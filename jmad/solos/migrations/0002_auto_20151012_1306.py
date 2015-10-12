# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='artist',
            field=models.CharField(max_length=100, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='instrument',
            field=models.CharField(max_length=50, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='track',
            field=models.CharField(max_length=100, default=None),
            preserve_default=False,
        ),
    ]
