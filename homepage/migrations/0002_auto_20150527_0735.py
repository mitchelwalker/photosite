# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='albums',
            field=models.ManyToManyField(to='homepage.Album'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to=b"static/static_dirs/img/<class 'homepage.admin.Album'>"),
            preserve_default=True,
        ),
    ]
