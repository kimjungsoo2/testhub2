# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0012_auto_20150317_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='Updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
