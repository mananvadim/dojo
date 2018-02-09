# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 14:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20170713_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='наименование')),
                ('description', models.TextField(db_column='description', verbose_name='описание')),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
                ('contractor', models.ForeignKey(db_column='contractor', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'verbose_name': 'проект',
                'db_table': 'project',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('text', models.TextField(db_column='text', verbose_name='текст комментария')),
                ('project', models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, to='app.Project', verbose_name='проект')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'комментарий к проекту',
                'db_table': 'project_comment',
                'verbose_name_plural': 'комментарии к проектам',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatusForClientInfo',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('project', models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, to='app.Project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'строка истории статусов проекта для заказчика',
                'db_table': 'project_status_for_client_info',
                'verbose_name_plural': 'строки истории статусов проектов для заказчиков',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatusForContractor',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='наименование')),
                ('is_closed', models.BooleanField(db_column='is_closed', verbose_name='это закрывающий проект статус')),
                ('contractor', models.ForeignKey(db_column='contractor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'verbose_name': 'статус проекта для исполнителя',
                'db_table': 'project_status_for_contractor',
                'verbose_name_plural': 'статусы проектов для исполнителей',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatusForContractorInfo',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('project', models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, to='app.Project', verbose_name='проект')),
                ('status', models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, to='app.ProjectStatusForContractor', verbose_name='статус')),
            ],
            options={
                'verbose_name': 'строка истории статусов проекта для исполнителя',
                'db_table': 'project_status_for_contractor_info',
                'verbose_name_plural': 'строки истории статусов проектов для исполнителей',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='наименование')),
                ('description', models.TextField(db_column='description', verbose_name='описание')),
                ('project', models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, to='app.Project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'задача',
                'db_table': 'task',
                'verbose_name_plural': 'задачи',
            },
        ),
        migrations.RenameModel(
            old_name='ClientProjectStatusForClient',
            new_name='ProjectStatusForClient',
        ),
        migrations.RemoveField(
            model_name='clientproject',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientproject',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='clientproject',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='clientprojectcomment',
            name='client_project',
        ),
        migrations.RemoveField(
            model_name='clientprojectcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='clientprojectstatusforclientinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clientprojectstatusforclientinfo',
            name='сlient_project',
        ),
        migrations.RemoveField(
            model_name='clientprojectstatusforcontractor',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='clientprojectstatusforcontractorinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clientprojectstatusforcontractorinfo',
            name='сlient_project',
        ),
        migrations.RemoveField(
            model_name='contractorproject',
            name='client_project',
        ),
        migrations.AlterModelOptions(
            name='projectstatusforclient',
            options={'verbose_name': 'статус проекта для заказчика', 'verbose_name_plural': 'статусы проектов для заказчиков'},
        ),
        migrations.AlterModelTable(
            name='projectstatusforclient',
            table='project_status_for_client',
        ),
        migrations.DeleteModel(
            name='ClientProject',
        ),
        migrations.DeleteModel(
            name='ClientProjectComment',
        ),
        migrations.DeleteModel(
            name='ClientProjectStatusForClientInfo',
        ),
        migrations.DeleteModel(
            name='ClientProjectStatusForContractor',
        ),
        migrations.DeleteModel(
            name='ClientProjectStatusForContractorInfo',
        ),
        migrations.DeleteModel(
            name='ContractorProject',
        ),
        migrations.AddField(
            model_name='projectstatusforclientinfo',
            name='status',
            field=models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, to='app.ProjectStatusForClient', verbose_name='статус'),
        ),
    ]
