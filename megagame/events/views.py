from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User

from events.models import Event
from articles.models import Article

import datetime

def get_event_list(request) -> JsonResponse:
	events = Event.objects.all()
	return JsonResponse(events)

def get_event(request, event_id: int) -> JsonResponse:
	event = Event.objects.get(id=event_id)
	return JsonResponse(event)

def get_event_news_list(request, event_id: int) -> JsonResponse:
	event = Event.objects.get(id=event_id)
	articles = Article.objects.get(event=event)
	return JsonResponse(articles)

def create_new_event(
	request, event_name: str,  event_description: str,
	event_created_by: int, event_start_date: str=None) -> None:
	creator = User.objects.get(id=event_created_by)
	new_event = Event(
		name=event_name,
		description=event_description,
		start_date=event_start_date,
		creation_date=datetime.datetime.now(),
		created_by=creator,
	)
	new_event.save()

def update_event(request) -> None:
	pass

def delete_event(request, event_id: int) -> None:
	pass