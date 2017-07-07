# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0003_auto_20170706_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='pool.Question'),
        ),
    ]
