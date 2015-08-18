# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0003_remove_testexecution_component_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='Component_ID',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
