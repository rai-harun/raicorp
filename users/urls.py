from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    #including default auth urls
    # path('', include('django.contrib.auth.urls')),

    #login
    path('login/', views.LoginUser, name="login"),

    #logout
    path('logout/', views.LogoutUser, name='logout'),
    #registration page
    path('register/', views.RegisterUser, name="registeruser"),
    path('profiledetails/<str:pk>/', views.ProfileDetails, name="profiledetails"),
]


