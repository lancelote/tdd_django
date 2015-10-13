# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0003_auto_20151013_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]
