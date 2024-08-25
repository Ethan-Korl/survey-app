from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository
from main.serializers import CreateSurveySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

survey_repo =  SurveyRepository


class ListSurveyView(ListAPIView):
    serializer_class = ""
    authentication_classes = []
    
    def get(self, request, *args, **kwargs):
        surveys = survey_repo.get_all_by_user(request.user.id)
        serializer = self.serializer_class(surveys, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class CreateSurveyView(CreateAPIView):
    serializer_class = CreateSurveySerializer
    authentication_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                context = {"detail": "Survey created"}
                return Response(data=context, status=status.HTTP_201_CREATED)
            
        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
            
        return super().post(request, *args, **kwargs)
    