# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homepage.admin


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_image_thumbnail2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to=homepage.models.only_filename),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail2',
            field=models.ImageField(null=True, upload_to=homepage.models.only_filename, blank=True),
            preserve_default=True,
        ),
    ]
