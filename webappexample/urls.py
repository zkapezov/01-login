from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("userhub/callback", views.userhub_callback, name="userhub_callback"),
    path("userhub/webhook", views.userhub_webhook, name="userhub_webhook"),
]
