# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-26 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20181126_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedmailids',
            name='mailid',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]