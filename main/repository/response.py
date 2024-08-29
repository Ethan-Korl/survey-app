from typing import Optional
from main.models import SelectionResponse, Question, Options
from main.models import ImageResponse
from main.models import TextResponse
from main.models import FileResponse, NumberResponse


class OptionsRepository:
    """
    Repository class for managing Options instances.
    """

    option_model = Options

    @classmethod
    def get_by_id(cls, option_id: int) -> Optional[Options]:
        try:
            return cls.option_model.objects.get(pk=option_id)
        except cls.option_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[Options]:
        return cls.option_model.objects.filter(question=question)

    @classmethod
    def create(
        cls,
        question: Question,
        option: str,
    ) -> Options:
        option_instance = cls.option_model.objects.create(
            question=question, option=option
        )
        option_instance.save()
        return option_instance


class TextResponseRepository:
    """
    Repository class for managing TextResponse instances.
    """

    text_response_model = TextResponse

    @classmethod
    def get_by_id(cls, response_id: int) -> Optional[TextResponse]:
        """
        Retrieve a TextResponse instance by its ID.
        """
        try:
            return cls.text_response_model.objects.get(pk=response_id)
        except cls.text_response_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[TextResponse]:
        """
        Retrieve all TextResponse instances associated with a given Question.
        """
        return cls.text_response_model.objects.filter(question=question)

    @classmethod
    def create(
        cls,
        question: Question,
        response_text: str,
    ) -> TextResponse:

        text_response_instance = cls.text_response_model.objects.create(
            question=question, response=response_text
        )
        text_response_instance.save()
        return text_response_instance


class ImageResponseRepository:
    """
    Repository class for managing ImageResponse instances.
    """

    image_response_model = ImageResponse

    @classmethod
    def get_by_id(cls, response_id: int) -> Optional[ImageResponse]:
        try:
            return cls.image_response_model.objects.get(pk=response_id)
        except cls.image_response_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[ImageResponse]:
        return cls.image_response_model.objects.filter(question=question)

    @classmethod
    def create(
        cls,
        question: Question,
        response_image: str,
    ) -> ImageResponse:
        response_instance = cls.image_response_model.objects.create(
            question=question, response=response_image
        )
        response_instance.save()
        return response_instance


class FileResponseRepository:
    """
    Repository class for managing FileResponse instances.
    """

    file_response_model = FileResponse

    @classmethod
    def get_by_id(cls, response_id: int) -> Optional[FileResponse]:
        try:
            return cls.file_response_model.objects.get(pk=response_id)
        except cls.file_response_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[FileResponse]:
        return cls.file_response_model.objects.filter(question=question)

    @classmethod
    def create(
        cls,
        question: Question,
        response_file: str,
    ) -> FileResponse:
        response_instance = cls.file_response_model.objects.create(
            question=question, response=response_file
        )
        response_instance.save()
        return response_instance


class NumberResponseRepository:
    """
    Repository class for managing NumberResponse instances.
    """

    number_response_model = NumberResponse

    @classmethod
    def get_by_id(cls, response_id: int) -> Optional[NumberResponse]:
        try:
            return cls.number_response_model.objects.get(pk=response_id)
        except cls.number_response_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[NumberResponse]:
        return cls.number_response_model.objects.filter(question=question)

    @classmethod
    def create(cls, question: Question, response: int):
        return cls.number_response_model.objects.create(
            question=question, response=response
        )


class SelectionResponseRepository:
    """
    Repository class for managing SelectionResponse instances.
    """

    selection_response_model = SelectionResponse

    @classmethod
    def get_by_id(cls, response_id: int) -> Optional[SelectionResponse]:
        try:
            return cls.selection_response_model.objects.get(pk=response_id)
        except cls.selection_response_model.DoesNotExist:
            return None

    @classmethod
    def get_by_question(cls, question: Question) -> list[SelectionResponse]:
        return cls.selection_response_model.objects.filter(question=question)

    @classmethod
    def create(
        cls,
        question: Question,
        response_option: Options,
    ) -> SelectionResponse:
        response_instance = cls.selection_response_model.objects.create(
            question=question, response=response_option
        )
        response_instance.save()
        return response_instance
