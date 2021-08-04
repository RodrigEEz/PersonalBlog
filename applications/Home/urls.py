from django.contrib import admin
from django.urls import path, include, re_path
from .views import HomePageView

app_name = "home"

urlpatterns = [
    path('', HomePageView.as_view(), name="home")
    ]