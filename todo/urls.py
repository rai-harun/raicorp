from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="todohome"),
    path('todoadd/', views.TodoAdd, name="todoadd"),
    path('tododelete/<int:pk>/', views.TodoDelete, name='tododelete'),
    path('todoedit/<int:pk>/', views.TodoEdit, name="todoedit"),
    path('todocomplete/<int:pk>/', views.TodoComplete, name="todocomplete")
]