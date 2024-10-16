# Generated by Django 5.1.2 on 2024-10-17 10:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualCourseStrike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('day_name', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10, verbose_name='Day Name')),
                ('battery_status', models.CharField(choices=[(0, 'zero'), (1, 'One'), (2, 'Two')], default=0, max_length=4)),
                ('length', models.SmallIntegerField(verbose_name='Length')),
                ('expired_at', models.DateField(verbose_name='Expired At')),
                ('strike_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualCourseStrikeHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('day_name', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10, verbose_name='Day Name')),
                ('battery_status', models.CharField(choices=[(0, 'zero'), (1, 'One'), (2, 'Two')], default=0, max_length=4)),
                ('expired_at', models.DateField(verbose_name='Expired At')),
                ('strike_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
