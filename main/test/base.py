from django.urls import reverse
from accounts.models import SurveyAdmin
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient
from django.test import TestCase
from main.models import Survey, Question
from django.test import TestCase, Client
from django.urls import reverse
from main.repository import SurveyRepository, QuestionRepository
from main.repository import QuestionRepository
