"""
utils related questions
"""

from main.repository import QuestionRepository

ques_repo = QuestionRepository


def check_if_required(answer_required):
    if answer_required is not None:
        return True
    return False

    # if str(type_of_response_required).upper() == "TEXT":

    # if str(type_of_response_required).upper() == "SELECTION":

    # if str(type_of_response_required).upper() == "FILE":

    # if str(type_of_response_required).upper() == "IMAGE":
