# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0002_auto_20150315_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testexecution',
            name='Component_ID',
        ),
    ]
