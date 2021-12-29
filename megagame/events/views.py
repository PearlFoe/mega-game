from typing import Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
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

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
def update_event(request) -> None:
	pass

@login_required(login_url='login_page')
def delete_event(request, event_id: int) -> None:
	pass

# ARTICLES

def get_article_list(request, event_id: int) -> HttpResponse:
	form = ArticleForm()
	event = get_object_or_404(Event, id=event_id)
	try:
		articles = Article.objects.filter(event=event)
	except ObjectDoesNotExist:
		articles = []
	finally:
		return render(request, 'articles/all_articles.html', {'articles': articles, 'form': form, 'event': event})

def get_new_articles(request, event_id: int, last_article_id: int=None) -> JsonResponse:
	event = Event.objects.filter(id=event_id).first()
	if not event:
		return JsonResponse({'success': False, 'error': 'Event was not found'}, status=400)

	last_article = Article.objects.get(id=last_article_id)
	if last_article:
		new_articles = Article.objects.filter(event=event, creation_date__gt=last_article.creation_date)
	else:
		new_articles = Article.objects.filter(event=event)

	return JsonResponse({'success': True, 'artiles': new_articles}, status=201)

@login_required(login_url='login_page')
def create_new_article(request, event_id: int) -> JsonResponse:
	if request.method == 'POST' and request.is_ajax():
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

			return JsonResponse({'success': True}, status=201)
		else:
			error = form.errors.as_json()
			return JsonResponse({'success': False, 'error': error}, status=400)
	else:
		return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

@login_required(login_url='login_page')
def delete_article(request, article_id: int) -> None:
	pass

@login_required(login_url='login_page')
def update_article(request) -> None:
	pass

def check_new_articles(request):
	pass