# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0006_auto_20150316_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='Num',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
