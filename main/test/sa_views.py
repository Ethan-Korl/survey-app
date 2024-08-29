from django.test import TestCase, Client
from django.urls import reverse
from main.models import Survey, Question
from accounts.models import SurveyAdmin
from django.contrib.auth.hashers import make_password
from main.repository import SurveyRepository, QuestionRepository


class SurveyAdminViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Setup some test data
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )
        self.survey = Survey.objects.create(
            admin=self.admin, title="Test Survey", description="small testing"
        )
        self.question = Question.objects.create(
            survey=self.survey,
            type_of_response_required="Text",
        )

    def test_sa_dashboard_renders_correct_template(self):
        url = reverse("sa-dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_dashboard.html")

    def test_survey_detail_renders_correct_template(self):
        url = reverse("survey-detail", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "survey_detail.html")
        self.assertContains(response, self.survey.title)
        self.assertContains(response, self.survey.description)

    def test_create_question_renders_correct_template(self):
        url = reverse("create-question", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_questions.html")

    def test_create_options_renders_correct_template(self):
        url = reverse("create-options", kwargs={"question_id": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_question_options.html")
        # self.assertContains(response, self.question.text)

    def test_survey_questions_renders_correct_template(self):
        url = reverse("survey-questions", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "survey_questions.html")

    def test_question_results_renders_correct_template(self):
        url = reverse("question-results", kwargs={"question_id": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_question_responses.html")
