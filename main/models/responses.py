from django.db import models
from main.models.questions import Question


# for questions that have option
class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)
    

class ImageReponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ImageField()
    
    
    
class SelectionResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Options, on_delete=models.CASCADE)
    
    


