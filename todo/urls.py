from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="todohome"),
    path('todoadd/', views.TodoAdd, name="todoadd"),
    path('tododelete/<int:pk>/', views.TodoDelete, name='tododelete'),
]