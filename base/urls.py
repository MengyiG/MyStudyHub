from django.urls import path
from . import views

# urlpatterns is a list of paths, each path is a tuple, the first element is the path
# the second element is the view function
# it determines which view function to call based on the URL requested
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),
    # the <str:pk> part of the URL is a path converter
    # The path converter <str:pk> will match any string
    # (except for the / character, which separates path segments).
    # The matched string will be stored in the pk variable
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deteleRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deteleMessage, name='delete-message'),
    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
]
