# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 21:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ticket_ticket_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_ticket_no', models.CharField(max_length=50, unique=True)),
                ('event_ticket_taken', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='TicketBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_idf', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='ID number must be numeric and eight characters', regex='^(\\d{7}|\\d{8})$')], verbose_name='Identification Number')),
                ('profile_phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Incorrect Phone Number', regex='^(0+[7]{1}[0-9]{8})$')], verbose_name='Phone Number')),
                ('number_of_tickets', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter a valid number', regex='^(\\d{1,5})$')])),
                ('ticket_confirmed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='event_id',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.AddField(
            model_name='eventticket',
            name='event_booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TicketBooking'),
        ),
    ]
