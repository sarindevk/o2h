# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-22 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170708_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc_mal',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
    ]
