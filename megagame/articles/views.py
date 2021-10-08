from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User

from events.models import Event
from articles.models import Article

import datetime

def get_article_list(request, event_id: int) -> JsonResponse:
    event = Event.objects.get(id=event_id)
    articles = Article.objects.get(event=event)

    return JsonResponse(articles)

def create_new_article(request) -> None:
    pass

def delete_article(request, article_id: int) -> None:
    pass

def update_article(request) -> None:
    pass

def check_new_articles(request):
    pass