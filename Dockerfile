# simple docker file to build the sqlbin

FROM python:3.11.4-slim-buster

LABEL version="survey_app 1.0"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "" ]

