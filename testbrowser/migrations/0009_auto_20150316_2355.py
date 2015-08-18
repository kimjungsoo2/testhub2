# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0008_auto_20150316_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarydomain',
            name='name',
            field=models.CharField(max_length=128, unique=True, null=True),
            preserve_default=True,
        ),
    ]
