# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 23:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0014_auto_20171130_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='governance_doc',
            name='record_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
