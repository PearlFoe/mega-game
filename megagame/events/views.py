from typing import Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

from events.models import Event, Article

import datetime
import pytz

# EVENTS

def get_event_list(request) -> HttpResponse:
	events = Event.objects.all()
	return render(request, 'events/all_events.html', {'events': events})

def get_event(request, event_id: int) -> JsonResponse:
	event = get_object_or_404(Event, id=event_id)
	return JsonResponse({'evet': dir(event)})

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

def update_event(request) -> None:
	pass

def delete_event(request, event_id: int) -> None:
	pass

# ARTICLES

def get_article_list(request, event_id: int) -> JsonResponse:
	event = get_object_or_404(Event, id=event_id)
	articles = []
	try:
		articles = Article.objects.get(event=event)
	except ObjectDoesNotExist:
		pass
	finally:
		return JsonResponse({'articles': articles})

def create_new_article(request) -> None:
	pass

def delete_article(request, article_id: int) -> None:
	pass

def update_article(request) -> None:
	pass

def check_new_articles(request):
	pass