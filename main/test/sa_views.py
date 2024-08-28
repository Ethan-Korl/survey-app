from django.test import TestCase, Client
from django.urls import reverse
from main.models import Survey, Question
from main.repository import SurveyRepository, QuestionRepository


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Setup some test data
        self.survey = Survey.objects.create(title="Test Survey")
        self.question = Question.objects.create(
            text="Test Question", survey=self.survey
        )

        # Mock the repository methods
        self.survey_repo = SurveyRepository()
        self.que_repo = QuestionRepository()

        # Mock the get_by_id method to return the test data
        self.survey_repo.get_by_id = lambda id: (
            self.survey if id == self.survey.id else None
        )
        self.que_repo.get_by_id = lambda id: (
            self.question if id == self.question.id else None
        )

    def test_sa_dashboard_renders_correct_template(self):
        url = reverse("sa_dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_dashboard.html")

    def test_survey_detail_renders_correct_template(self):
        url = reverse("survey_detail", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "survey_detail.html")
        self.assertContains(response, self.survey.title)

    def test_create_question_renders_correct_template(self):
        url = reverse("create_question", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_questions.html")

    def test_create_options_renders_correct_template(self):
        url = reverse("create_options", kwargs={"question_id": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_question_options.html")
        self.assertContains(response, self.question.text)

    def test_survey_questions_renders_correct_template(self):
        url = reverse("survey_questions", kwargs={"survey_id": self.survey.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "survey_questions.html")

    def test_question_results_renders_correct_template(self):
        url = reverse("question_results", kwargs={"question_id": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_question_responses.html")
