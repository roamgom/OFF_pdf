# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20171111_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publish Date'),
        ),
    ]
