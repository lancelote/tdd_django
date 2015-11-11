# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['album', 'track_number']},
        ),
    ]
