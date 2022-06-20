from django.urls import path
from django import forms
from django.contrib.auth.models import User

from . import views

app_name = "profiles"

urlpatterns = [
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
]
