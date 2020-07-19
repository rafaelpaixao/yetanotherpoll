"""yap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

from .apps.polls.views import create_poll, edit_poll, get_poll, get_poll_results, get_user_polls, vote_on_poll
from .apps.users.views import LoginView, register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/register/", register, name="register"),
    path("api/poll/", get_user_polls, name="get_user_polls"),
    path("api/poll/create/", create_poll, name="create_poll"),
    path("api/poll/<int:poll_id>/", get_poll, name="get_poll"),
    path("api/poll/<int:poll_id>/edit/", edit_poll, name="edit_poll"),
    path("api/poll/<int:poll_id>/results/", get_poll_results, name="get_poll_results"),
    path("api/vote/<int:option_id>/", vote_on_poll, name="vote_on_poll"),
]
