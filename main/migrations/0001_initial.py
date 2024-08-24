# Generated by Django 5.1 on 2024-08-24 09:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('survey_link', models.URLField(blank=True, null=True)),
                ('date_crated', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('close_survey', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_answer_required', models.CharField(choices=[], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('make_available', models.BooleanField(default=False)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey')),
            ],
        ),
    ]
