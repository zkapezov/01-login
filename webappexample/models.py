from django.db import models


class Subscription(models.Model):
    user_email = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
