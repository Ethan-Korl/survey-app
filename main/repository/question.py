from main.models import Question
from main.models import Survey
from typing import Optional


class QuestionRepository:
    """
    Repository class for managing Question instances.
    """

    question_model = Question

    @classmethod
    def get_by_id(cls, question_id: int) -> Optional[Question]:
        try:
            return cls.question_model.objects.get(pk=question_id)
        except cls.question_model.DoesNotExist:
            return None

    @classmethod
    def get_by_survey(cls, survey: Survey) -> list[Question]:
        return cls.question_model.objects.filter(survey=survey)

    @classmethod
    def create(
        cls,
        survey: Survey,
        question: str,
        type_of_response_required: str,
        max_length=None,
        min_value=None,
        max_value=None,
        answer_required: bool = False,
    ) -> Question:

        question = cls.question_model.objects.create(
            question=question,
            max_value=max_value,
            min_value=min_value,
            max_length=max_length,
            survey=survey,
            type_of_response_required=type_of_response_required,
            answer_required=answer_required,
        )
        question.save()
        return question

    @classmethod
    def delete(cls, question_id: int) -> bool:
        try:
            question = cls.get_by_id(question_id)
            if question:
                question.delete()
                return True
        except Exception:
            pass
        return False
