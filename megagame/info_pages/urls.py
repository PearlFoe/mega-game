from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index_page'),
	path('rules/', views.rules, name='rules_page'),
]