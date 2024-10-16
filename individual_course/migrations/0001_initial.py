# Generated by Django 5.1.2 on 2024-10-16 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('individual_course_group', '0001_initial'),
        ('role_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('index', models.IntegerField(verbose_name='Index')),
                ('prerequisite', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='individual_course.individualcourse', verbose_name='Prerequisite')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Edit Date')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('enable_completed', models.BooleanField(default=False, verbose_name='Enable Completed')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Score')),
                ('individual_course_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual_course_group.individualcoursegroup', verbose_name='Individual Course Group')),
                ('role', models.ManyToManyField(to='role_management.role', verbose_name='Role')),
            ],
        ),
    ]
