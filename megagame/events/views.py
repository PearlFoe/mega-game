from typing import Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

from events.models import Event, Article
from events.forms import ArticleForm

import datetime
import pytz

# EVENTS

def get_event_list(request) -> HttpResponse:
	events = Event.objects.all()
	return render(request, 'events/all_events.html', {'events': events})

def get_event(request, event_id: int) -> JsonResponse:
	event = get_object_or_404(Event, id=event_id)
	return render(request, 'events/event.html', {'event': event})

@login_required
def create_new_event(
	request, event_name: str,  event_description: str,
	event_created_by: int, event_start_date: str=None) -> None:
	creator = User.objects.get(id=event_created_by)
	new_event = Event(
		name=event_name,
		description=event_description,
		start_date=event_start_date,
		creation_date=datetime.datetime.now(pytz.timezone("Europe/Moscow")),
		created_by=creator,
	)
	new_event.save()

@login_required
def update_event(request) -> None:
	pass

@login_required
def delete_event(request, event_id: int) -> None:
	pass

# ARTICLES

def get_article_list(request, event_id: int) -> HttpResponse:
	form = ArticleForm()
	event = get_object_or_404(Event, id=event_id)
	try:
		articles = Article.objects.all().filter(event=event)
	except ObjectDoesNotExist:
		articles = []
	finally:
		return render(request, 'articles/all_articles.html', {'articles': articles, 'form': form, 'event': event})

@login_required
def create_new_article(request, event_id: int) -> HttpResponse:
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form_data = form.split_header_and_body()
			if isinstance(form_data, list):
				title, body = form_data
			else:
				title = form_data
				body = None
			
			current_event = get_object_or_404(Event, id=event_id)
			current_user = request.user
			new_article = Article(
				title=title,
				description=body,
				creation_date=datetime.datetime.now(pytz.timezone("Europe/Moscow")),
				created_by=current_user,
				event=current_event,
			)
			new_article.save()

			return HttpResponse(status=201)
		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=405)

@login_required
def delete_article(request, article_id: int) -> None:
	pass

@login_required
def update_article(request) -> None:
	pass

def check_new_articles(request):
	pass