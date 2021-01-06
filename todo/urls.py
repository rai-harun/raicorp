from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeLanding, name="HomeLanding"),
    path('todo/<int:pk>/', views.Home, name="todohome"),
    path('todoadd/', views.TodoAdd, name="todoadd"),
    path('tododelete/<int:pk>/', views.TodoDelete, name='tododelete'),
    path('todoedit/<int:pk>/', views.TodoEdit, name="todoedit"),
    path('todocomplete/<int:pk>/', views.TodoComplete, name="todocomplete")
]