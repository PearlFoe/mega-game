from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('Index page!')

def rules(request):
    return HttpResponse('Rules page!')