import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
d = datetime.today() - timedelta(hours=0, minutes=50)


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    code = models.CharField(max_length=8)
    uid_scheduler = models.CharField(default='', max_length=255)
    interval_notify = models.IntegerField()
    higher_limit = models.FloatField()
    lower_limit = models.FloatField()
    sync = models.BooleanField(default=False)
    last_notification = models.DateTimeField(
        auto_now=False, default=d.isoformat())
