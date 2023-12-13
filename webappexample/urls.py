from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("userhub/callback", views.userhub_callback, name="userhub_callback"),
    path("userhub/webhook", views.userhub_webhook, name="userhub_webhook"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
