from main.test.base import *


class QuestionRepositoryTests(TestCase):
    def setUp(self):
        """
        Set up a test survey and a few questions for testing.
        """
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )

        self.survey = Survey.objects.create(
            admin=self.admin,
            title="Test Survey",
            description="A description of the test survey.",
            close_survey=False,
        )

        self.question1 = Question.objects.create(
            survey=self.survey,
            type_of_response_required="Multiple Choice",
        )

        self.question2 = Question.objects.create(
            survey=self.survey,
            type_of_response_required="Text",
        )

    def test_get_by_id(self):
        """
        Test retrieval of a Question by ID.
        """
        question = QuestionRepository.get_by_id(self.question1.id)
        self.assertIsNotNone(question)
        self.assertEqual(question.id, self.question1.id)
        self.assertEqual(question.type_of_response_required, "Multiple Choice")

    def test_get_by_survey(self):
        """
        Test retrieval of Questions by Survey.
        """
        questions = QuestionRepository.get_by_survey(self.survey)
        self.assertEqual(len(questions), 2)
        self.assertIn(self.question1, questions)
        self.assertIn(self.question2, questions)

    def test_create(self):
        """
        Test creation of a new Question.
        """
        new_question = QuestionRepository.create(
            question="Who are you",
            survey=self.survey,
            type_of_response_required="Text",
            answer_required=True,
        )
        self.assertIsNotNone(new_question)
        self.assertEqual(new_question.type_of_response_required, "Text")
        self.assertEqual(new_question.survey, self.survey)
        self.assertEqual(new_question.question, "Who are you")

    def test_delete(self):
        """
        Test deletion of a Question.
        """
        success = QuestionRepository.delete(self.question1.id)
        self.assertTrue(success)
        self.assertIsNone(QuestionRepository.get_by_id(self.question1.id))

        # Try deleting again to ensure it fails gracefully
        success = QuestionRepository.delete(self.question1.id)
        self.assertFalse(success)
