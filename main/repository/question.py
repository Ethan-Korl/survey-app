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
    def create(cls, survey: Survey, 
               type_of_response_required: str, 
               make_available: bool = False) -> Question:
        
        question = cls.question_model.objects.create(
            survey=survey,
            type_of_response_required=type_of_response_required,
            make_available=make_available
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
