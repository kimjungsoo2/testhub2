# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0005_auto_20150315_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='Status_ID',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
