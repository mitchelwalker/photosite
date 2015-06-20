# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20150527_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
