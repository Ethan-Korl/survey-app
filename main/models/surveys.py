from django.urls import resolve, reverse
from uuid import uuid4
from django.db import models

class Survey(models.Model):
    url_id = models.UUIDField(default=uuid4, unique=True)
    title = models.CharField(max_length=50, unique=True, verbose_name="name")
    description = models.CharField(max_length=100, null=True, blank=True)
    survey_link = models.URLField(null=True, blank=True)
    date_crated = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    close_survey = models.BooleanField(default=False)
    
    
    def generate_url(self):
        url = reverse('sp-dashboard', kwargs={'url_id':self.url_id})
        print(url)
        self.survey_link = url
        self.save()



