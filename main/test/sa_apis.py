from main.test.base import *


class TestSurveyAdminApis(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )

    def test_that_list_survey_view_is_protected(self):
        url = reverse("list-survey-api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    # def test_list_survey_view(self):
    #     url = reverse("list-survey-api")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 401)
