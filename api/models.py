from django.db import models
from django.utils.timezone import now


class Recording(models.Model):
    when = models.DateTimeField(default=now)
    rating = models.FloatField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.when.__str__()
