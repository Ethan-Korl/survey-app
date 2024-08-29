# survey-app
Survey app

# Projecct Structure

```plaintext
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

15 directories, 67 files


# Testing

```bash
./manage.py test

python manage.py test
```
