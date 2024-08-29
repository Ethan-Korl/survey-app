from main.test.base import *


class SpDashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )
        self.survey = Survey.objects.create(admin=self.admin, title="Test Survey")

    def test_sp_dashboard_renders_correct_template(self):
        """
        Check if sp dashboard is up
        """
        url = reverse("sp-dashboard", kwargs={"url_id": self.survey.url_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "sp_response.html")
