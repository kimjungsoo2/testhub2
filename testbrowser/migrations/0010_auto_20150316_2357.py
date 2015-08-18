# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0009_auto_20150316_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarydomain',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 3, 16, 23, 57, 19, 439615), unique=True, max_length=128),
            preserve_default=False,
        ),
    ]
