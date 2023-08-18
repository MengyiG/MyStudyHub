from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # the <str:pk> part of the URL is a path converter
    # The path converter <str:pk> will match any string
    # (except for the / character, which separates path segments).
    # The matched string will be stored in the pk variable
    path('room/<str:pk>/', views.room, name='room'),
]
