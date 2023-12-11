from django.urls import path
from .views import *
app_name = "accounts"


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




urlpatterns=[
    path('home',HomeView.as_view(),name="home"),
    path('login',LoginView.as_view(),name="login"),
    path('register',RegisterView.as_view(),name='register'),
    path('otp',OtpView.as_view(),name="otp"),
    path('logout',LogoutView,name="logout"),
]