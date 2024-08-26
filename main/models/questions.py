
from django.utils import choices
from .surveys import  Survey
from django.db import models

ANSWER_TPYES = []

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    type_of_reponse_required = models.CharField(choices=ANSWER_TPYES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    make_available = models.BooleanField(default=False)




    


    
