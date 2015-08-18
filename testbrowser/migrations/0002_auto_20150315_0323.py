# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbrowser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Resolution_ID', models.IntegerField(null=True)),
                ('Due', models.DateTimeField(null=True)),
                ('Priority', models.IntegerField(null=True)),
                ('Type', models.CharField(max_length=255)),
                ('Secondary_domain_name', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('Updated', models.DateTimeField(null=True)),
                ('Primary_domain_name', models.CharField(max_length=255)),
                ('Regression_Level', models.CharField(max_length=255, null=True)),
                ('Reporter', models.CharField(max_length=255)),
                ('Project_Key', models.CharField(max_length=255)),
                ('Status_ID', models.IntegerField()),
                ('Key', models.CharField(unique=True, max_length=255)),
                ('Num', models.IntegerField()),
                ('Project_ID', models.IntegerField()),
                ('Requirements_Traceability', models.TextField(null=True)),
                ('Created', models.DateTimeField(null=True)),
                ('Summary', models.TextField()),
                ('Type_ID', models.IntegerField()),
                ('Component_ID', models.TextField()),
                ('Resolution', models.CharField(max_length=255, null=True)),
                ('Description', models.TextField(null=True)),
                ('Project', models.CharField(max_length=255)),
                ('Labels', models.TextField(null=True)),
                ('Assignee', models.CharField(max_length=255, null=True)),
                ('Components', models.TextField()),
                ('Primary_domain_key', models.ForeignKey(to='testbrowser.Primarydomain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Test_Case_ID', models.CharField(max_length=255)),
                ('Resolution_ID', models.CharField(max_length=255, null=True)),
                ('Due', models.CharField(max_length=255, null=True)),
                ('Priority', models.CharField(max_length=255, null=True)),
                ('Type', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('Updated', models.DateTimeField()),
                ('Component_ID', models.CharField(max_length=255)),
                ('Description', models.TextField(null=True)),
                ('Reporter', models.CharField(max_length=255)),
                ('Project_Key', models.CharField(max_length=255)),
                ('Status_ID', models.IntegerField()),
                ('Test_Plan_CR', models.CharField(max_length=255)),
                ('Key', models.CharField(max_length=255)),
                ('Project_ID', models.IntegerField()),
                ('Created', models.DateTimeField()),
                ('Remote_Defect_CR', models.CharField(max_length=255, null=True)),
                ('Summary', models.TextField()),
                ('TypeID', models.IntegerField()),
                ('Resolution', models.CharField(max_length=255, null=True)),
                ('Project', models.CharField(max_length=255)),
                ('Labels', models.CharField(max_length=255, null=True)),
                ('Assignee', models.CharField(max_length=255, null=True)),
                ('Components', models.CharField(max_length=255, null=True)),
                ('Test_Results', models.CharField(max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testplan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testexecution',
            name='Test_Plan_Key',
            field=models.ForeignKey(to='testbrowser.Testplan'),
            preserve_default=True,
        ),
    ]
