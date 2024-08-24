from django.test import TestCase
from django.test import TestCase
from main.repository import SurveyRepository
from main.models import Survey

class SurveyRepositoryTests(TestCase):
    def setUp(self):
        """
        Set up a test survey instance for use in the tests.
        """
        self.repo = SurveyRepository()
        self.survey = Survey.objects.create(title="Test Survey")

    def test_get_by_id(self):
        survey = self.repo.get_by_id(self.survey.id)
        self.assertEqual(survey, self.survey)
        
        # Test for a non-existing ID
        non_existent_survey = self.repo.get_by_id(999)
        self.assertIsNone(non_existent_survey)

    def test_get_all(self):
        surveys = self.repo.get_all()
        self.assertIn(self.survey, surveys)

    def test_create(self):

        new_survey = self.repo.create(title="New Survey", close_survey=True)
        self.assertIsNotNone(new_survey.id)
        self.assertEqual(new_survey.title, "New Survey")
        self.assertTrue(new_survey.close_survey)

    def test_update(self):

        updated_survey = self.repo.update(self.survey.id, title="Updated Survey", close_survey=True)
        self.assertEqual(updated_survey.title, "Updated Survey")
        self.assertTrue(updated_survey.close_survey)
        
        # Test updating a non-existing survey
        non_existent_survey = self.repo.update(999, title="Does Not Exist")
        self.assertIsNone(non_existent_survey)

    def test_delete(self):

        result = self.repo.delete(self.survey.id)
        self.assertTrue(result)
        self.assertIsNone(self.repo.get_by_id(self.survey.id))
        
        # Test deleting a non-existing survey
        result = self.repo.delete(999)
        self.assertFalse(result)
