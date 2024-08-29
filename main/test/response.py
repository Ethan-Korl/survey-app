from main.test.base import *


class QuestionModelTest(TestCase):
    def setUp(self):
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )

        self.survey = Survey.objects.create(
            admin=self.admin,
            title="Test Survey",
            description="A description of the test survey.",
            close_survey=False,
        )
        self.que_repo = QuestionRepository
        self.option_repo = OptionsRepository
        self.selection_repo = SelectionResponseRepository
        self.text_repo = TextResponseRepository
        self.number_repo = NumberResponseRepository
        self.question = self.que_repo.create(
            question="Sample question",
            survey=self.survey,
            type_of_response_required="",
            answer_required=True,
        )


class OptionsRepositoryTest(QuestionModelTest):
    def test_create_option(self):
        option = self.option_repo.create(question=self.question, option="Option 1")
        self.assertEqual(option.option, "Option 1")
        self.assertEqual(option.question, self.question)

    def test_get_by_id(self):
        option = self.option_repo.create(question=self.question, option="Option 1")
        retrieved_option = self.option_repo.get_by_id(option.id)
        self.assertEqual(retrieved_option, option)

    def test_get_by_question(self):
        self.option_repo.create(question=self.question, option="Option 1")
        self.option_repo.create(question=self.question, option="Option 2")
        options = self.option_repo.get_by_question(self.question)
        self.assertEqual(len(options), 2)


class TextResponseRepositoryTest(QuestionModelTest):
    def test_create_text_response(self):
        text_response = self.text_repo.create(
            question=self.question, response_text="Sample response"
        )
        self.assertEqual(text_response.response, "Sample response")
        self.assertEqual(text_response.question, self.question)

    def test_get_by_id(self):
        text_response = self.text_repo.create(
            question=self.question, response_text="Sample response"
        )
        retrieved_response = self.text_repo.get_by_id(text_response.id)
        self.assertEqual(retrieved_response, text_response)

    def test_get_by_question(self):
        self.text_repo.create(question=self.question, response_text="Response 1")
        self.text_repo.create(question=self.question, response_text="Response 2")
        responses = self.text_repo.get_by_question(self.question)
        self.assertEqual(len(responses), 2)


class NumberResponseRepositoryTest(QuestionModelTest):
    def test_create_number_response(self):
        number_response = self.number_repo.create(question=self.question, response=42)
        self.assertEqual(number_response.response, 42)
        self.assertEqual(number_response.question, self.question)

    def test_get_by_id(self):
        number_response = self.number_repo.create(question=self.question, response=42)
        retrieved_response = self.number_repo.get_by_id(number_response.id)
        self.assertEqual(retrieved_response, number_response)

    def test_get_by_question(self):
        self.number_repo.create(question=self.question, response=42)
        self.number_repo.create(question=self.question, response=84)
        responses = self.number_repo.get_by_question(self.question)
        self.assertEqual(len(responses), 2)


class SelectionResponseRepositoryTest(QuestionModelTest):
    def test_create_selection_response(self):
        option = self.option_repo.create(question=self.question, option="Option 1")
        selection_response = self.selection_repo.create(
            question=self.question, response_option=option
        )
        self.assertEqual(selection_response.response, option)
        self.assertEqual(selection_response.question, self.question)

    def test_get_by_id(self):
        option = self.option_repo.create(question=self.question, option="Option 1")
        selection_response = self.selection_repo.create(
            question=self.question, response_option=option
        )
        retrieved_response = self.selection_repo.get_by_id(selection_response.id)
        self.assertEqual(retrieved_response, selection_response)

    def test_get_by_question(self):
        option1 = self.option_repo.create(question=self.question, option="Option 1")
        option2 = self.option_repo.create(question=self.question, option="Option 2")
        self.selection_repo.create(question=self.question, response_option=option1)
        self.selection_repo.create(question=self.question, response_option=option2)
        responses = self.selection_repo.get_by_question(self.question)
        self.assertEqual(len(responses), 2)
