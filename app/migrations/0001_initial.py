# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 13:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=60)),
                ('category_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=60)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='events/')),
                ('event_type', models.CharField(blank=True, max_length=60, null=True)),
                ('event_description', models.TextField()),
                ('event_location', models.CharField(max_length=60)),
                ('number_of_tickets', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Please enter a valid ticket number', regex='^(\\d{1,5})$')])),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('event_created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('event_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
            options={
                'ordering': ['-event_created_on'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=80)),
                ('profile_interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='app.Category')),
                ('profile_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
