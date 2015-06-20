# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20150527_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail2',
            field=models.ImageField(null=True, upload_to=b'/home/ubuntu/workspace/static/media/', blank=True),
            preserve_default=True,
        ),
    ]
