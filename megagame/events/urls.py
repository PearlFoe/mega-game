from django.urls import path, include

from . import views

urlpatterns = [
	path('all/', views.get_event_list, name='event_list_page'),
	path('<int:event_id>/', views.get_event, name='event_page'),

	path('<int:event_id>/article/all/', views.get_article_list, name='event_article_list_page'),
	path('<int:event_id>/article/create/', views.create_new_article, name='create_new_article_url')
]