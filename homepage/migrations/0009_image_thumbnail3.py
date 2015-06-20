# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20150528_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail3',
            field=models.ImageField(null=True, upload_to=homepage.models.only_filename, blank=True),
            preserve_default=True,
        ),
    ]
