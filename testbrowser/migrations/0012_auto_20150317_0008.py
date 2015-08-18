# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0011_remove_testexecution_component_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='Key',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
