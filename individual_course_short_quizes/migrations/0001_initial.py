# Generated by Django 5.1.2 on 2024-10-17 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('individual_course_enrollment', '0001_initial'),
        ('individual_course_templates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualShortQuiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('question', models.TextField(verbose_name='Question')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_templates.individualcoursetemplate', verbose_name='Individual Course Template')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualShorQuizSubmit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is Correct')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('score', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Score')),
                ('individual_course_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_enrollment.individualcourseenrolment', verbose_name='Individual Course Enrolment')),
                ('short_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_short_quizes.individualshortquiz', verbose_name='Individual Short Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualShorQuizPoints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('points_title', models.CharField(max_length=50, verbose_name='Points Title')),
                ('points_value', models.IntegerField(verbose_name='Points Value')),
                ('short_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_short_quizes.individualshortquiz', verbose_name='Individual Short Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualShorQuizOptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('text', models.CharField(max_length=255, verbose_name='Option Text')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is Correct')),
                ('short_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_short_quizes.individualshortquiz', verbose_name='Individual Short Quiz')),
            ],
        ),
    ]
