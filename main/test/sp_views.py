from django.test import TestCase, Client
from django.urls import reverse


class SpDashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sp_dashboard_renders_correct_template(self):
        """
        Check if sp dashboard is up
        """
        url = reverse("sp-dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sp_response.html")
