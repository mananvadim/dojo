# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-22 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170722_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatusforclient',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectstatusforclient',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatusforcontractor',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectstatusforcontractor',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatusinfoforclient',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectstatusinfoforclient',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatusinfoforcontractor',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectstatusinfoforcontractor',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskstatusinfo',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskstatusinfo',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskwork',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskwork',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='id',
            field=models.CharField(db_column='id', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='version',
            field=models.CharField(db_column='version', max_length=50, null=True),
        ),
    ]