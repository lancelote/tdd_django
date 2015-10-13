# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0002_auto_20151012_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='album',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='end_time',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='solo',
            name='start_time',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
