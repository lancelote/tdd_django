# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0005_auto_20151013_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solo',
            options={'ordering': ['track', 'start_time']},
        ),
        migrations.RemoveField(
            model_name='solo',
            name='album',
        ),
    ]
