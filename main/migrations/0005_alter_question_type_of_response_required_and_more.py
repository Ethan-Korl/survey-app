# Generated by Django 5.1 on 2024-08-28 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_anwser_required_question_answer_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type_of_response_required',
            field=models.CharField(choices=[('Text', 'Text'), ('Selection', 'Selection'), ('File', 'File'), ('Image', 'Image'), ('Number', 'Number')], max_length=50),
        ),
        migrations.CreateModel(
            name='NumberResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_responses', to='main.question')),
            ],
        ),
    ]
