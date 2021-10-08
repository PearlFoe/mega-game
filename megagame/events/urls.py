from django.urls import path

from . import views

urlpatterns = [
	path('all/', views.get_event_list, name='event_list_page'),
	path('<int:event_id>/', views.get_event, name='event_page'),
]