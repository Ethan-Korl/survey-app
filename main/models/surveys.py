

from django.contrib.auth.models import models

class Survey(models.Model):
    name = models.CharField(max_length=50)
    date_crated = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    close_survery = models.BooleanField(default=False)



