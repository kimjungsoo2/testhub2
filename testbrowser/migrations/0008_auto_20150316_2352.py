# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0007_auto_20150316_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='Component_ID',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Components',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Project_ID',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Summary',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Type_ID',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
