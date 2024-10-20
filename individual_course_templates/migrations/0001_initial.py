# Generated by Django 5.1.2 on 2024-10-17 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('individual_course_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualCourseTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('index', models.IntegerField(verbose_name='Index')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Score')),
                ('template_content', models.TextField()),
                ('next_template', models.BooleanField(default=False, verbose_name='Next Template')),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_contents.individualcoursecontents', verbose_name='Contents')),
            ],
        ),
        migrations.CreateModel(
            name='columnType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('type', models.CharField(choices=[('quiz', 'Quiz'), ('shortquiz', 'ShortQuiz'), ('textbook', 'TextBook')], max_length=50)),
                ('templates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_templates.individualcoursetemplate', verbose_name='Template')),
            ],
        ),
    ]
