# Hosted on
```
https://survey-app-yjrt.onrender.com
```
# Setup
```bash
cd survey-app
pip install requirements.txt
./manege.py makemigrations | python manage.py makemigrations
./manage.py migrate | python manage.py migrate
```
# Testing
```bash
./manage.py test | python manage.py test
```
# Running the program locally
```bash
./manage.py runserver | python manage.py runserver
```
# Running the docker image
```bash
docker pull bhigethan/survey_app:latest
docker run -p 8000:8000 \
-e POSTGRES_USER=<postgres_user> \
-e POSTGRES_DBNAM=<postgres_dbname> \
-e POSTGRES_USER_PASSWORD=<postgres_user_password> \
-e HOST=<host> \
-e PORT=<port> \
bhigethan/survey_app:latest
```
# Runnig in Production Environment
```bash
gunicorn SurveyApp.wsgi
```
# Swagger Documentation api 
```
/api/schema/swagger-ui/
```
# 16 directories, 68 files
# Projecct Structure
```plaintext
.
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── repository.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views
│       ├── __init__.py
│       └── views.py
├── auth_backend
│   ├── backends.py
│   ├── __init__.py
│   └── tests.py
├── db.sqlite3
├── Dockerfile
├── ImageResponses
│   └── Untitled.png
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── questions.py
│   │   ├── responses.py
│   │   └── surveys.py
│   ├── repository
│   │   ├── __init__.py
│   │   ├── question.py
│   │   ├── response.py
│   │   └── survey.py
│   ├── serializers
│   │   ├── __init__.py
│   │   ├── question.py
│   │   ├── response.py
│   │   └── survey.py
│   ├── test
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── question.py
│   │   ├── response.py
│   │   ├── sa_apis.py
│   │   ├── sa_views.py
│   │   ├── sp_views.py
│   │   └── survey.py
│   ├── urls
│   │   ├── __init__.py
│   │   ├── sa_urls.py
│   │   └── sp_urls.py
│   └── views
│       ├── __init__.py
│       ├── sa_dashboard_apis.py
│       ├── sa_dashboard_views.py
│       ├── sp_dashboard_apis.py
│       └── sp_dashboard_views.py
├── manage.py
├── README.md
├── requirements.txt
├── scripts
├── SurveyApp
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tailwind.config.js
├── templates
│   ├── sa_dashboard.html
│   ├── sa_login.html
│   ├── sa_question_options.html
│   ├── sa_question_responses.html
│   ├── sa_questions.html
│   ├── sa_register.html
│   ├── sp_response.html
│   ├── survey_detail.html
│   └── survey_questions.html
└── utils
    ├── general.py
    ├── __init__.py
    └── question.py

```