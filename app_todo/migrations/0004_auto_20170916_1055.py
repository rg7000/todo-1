# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0003_auto_20170916_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed_date',
            field=models.DateTimeField(blank=True, verbose_name='completed date'),
        ),
    ]
