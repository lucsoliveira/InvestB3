import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    code = models.CharField(max_length=8)
    interval_notify = models.IntegerField()
    higher_limit = models.FloatField()
    lower_limit = models.FloatField()
    sync = models.BooleanField(default=False)
    last_notification = models.DateTimeField(auto_now=True)
