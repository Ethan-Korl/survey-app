from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository
from main.serializers import CreateSurveySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status

survey_repo =  SurveyRepository


class ListSurveyView(ListAPIView):
    serializer_class = ""
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        surveys = survey_repo.get_all_by_user(request.user)
        serializer = self.serializer_class(surveys, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class CreateSurveyView(CreateAPIView):
    pagination_class = [MultiPartParser]
    serializer_class = CreateSurveySerializer
    model_repo = SurveyRepository
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                title = serializer.validated_data.get("title")
                description = serializer.validated_data.get("description")
                
                # check if survey name already exits(title in this case)
                if self.model_repo.get_by_title(title=title) is not None:
                    context = {"detail": "Survey with the same name exists"}
                    return Response(data=context, status=status.HTTP_409_CONFLICT)
                
                survey = self.model_repo.create(admin=request.user,
                                       title=title,
                                       description=description
                                       )
                context = {"detail": "Survey created"}
                return Response(data=context, status=status.HTTP_201_CREATED)
            
        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(context)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
            
        return super().post(request, *args, **kwargs)
    