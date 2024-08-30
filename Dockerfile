# simple docker file to build the survey_app

FROM python:3.11-alpine

LABEL version="survey_app 1.0"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "SurveyApp.wsgi" ]

