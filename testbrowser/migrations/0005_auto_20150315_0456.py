# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0004_testexecution_component_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='Component_ID',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
