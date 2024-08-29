from main.test.base import *


class SurveyRepositoryTests(TestCase):
    def setUp(self):
        """
        Set up a test survey instance for use in the tests.
        """
        self.repo = SurveyRepository()
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )
        self.survey = Survey.objects.create(admin=self.admin, title="Test Survey")

    def test_get_by_id(self):
        survey = self.repo.get_by_id(self.survey.id)
        self.assertEqual(survey, self.survey)

        # Test for a non-existing ID
        non_existent_survey = self.repo.get_by_id(999)
        self.assertIsNone(non_existent_survey)

    def test_get_all(self):
        surveys = self.repo.get_all_by_user(self.admin)
        self.assertIn(self.survey, surveys)

    def test_create(self):
        new_survey = self.repo.create(
            admin=self.admin,
            title="New Survey",
            description="my des",
            close_survey=True,
        )
        self.assertEqual(new_survey.description, "my des")
        self.assertIsNotNone(new_survey.id)
        self.assertEqual(new_survey.title, "New Survey")
        self.assertTrue(new_survey.close_survey)

    def test_delete(self):

        result = self.repo.delete(self.survey.id)
        self.assertTrue(result)
        self.assertIsNone(self.repo.get_by_id(self.survey.id))

        # Test deleting a non-existing survey
        result = self.repo.delete(999)
        self.assertFalse(result)
