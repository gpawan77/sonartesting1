from django.urls import path

from . import views

url_patterns = [
    path('', views.LocationListView.as_view(), name='list'),
]