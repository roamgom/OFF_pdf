# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 08:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='magazine_title',
        ),
        migrations.AddField(
            model_name='magazine',
            name='file',
            field=models.FileField(default='', upload_to='magazines/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='OFF Magazine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='magazine',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 11, 8, 47, 8, 669684, tzinfo=utc), verbose_name='Publish Date'),
        ),
    ]
