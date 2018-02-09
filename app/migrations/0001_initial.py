# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 11:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('text', models.TextField(db_column='text', verbose_name='текст комментария')),
            ],
            options={
                'db_table': 'comment',
                'verbose_name_plural': 'комментарии',
                'verbose_name': 'комментарий',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
                ('contractor', models.ForeignKey(db_column='contractor', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'db_table': 'contract',
                'verbose_name_plural': 'договоры',
                'verbose_name': 'договор',
            },
        ),
        migrations.CreateModel(
            name='StatusForClient',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('name', models.CharField(db_column='name', max_length=20, verbose_name='наименование')),
                ('is_closed', models.BooleanField(db_column='is_closed', verbose_name='закрыт')),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
            ],
            options={
                'db_table': 'status_for_client',
                'verbose_name_plural': 'статусы задач для заказчиков',
                'verbose_name': 'статус задачи для заказчика',
            },
        ),
        migrations.CreateModel(
            name='StatusForClientInfo',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('status', models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, to='app.StatusForClient', verbose_name='статус')),
            ],
            options={
                'db_table': 'status_for_client_info',
                'verbose_name_plural': 'строки истории статусов задач для заказчиков',
                'verbose_name': 'строка истории статусов задачи для заказчика',
            },
        ),
        migrations.CreateModel(
            name='StatusForContractor',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('name', models.CharField(db_column='name', max_length=20, verbose_name='наименование')),
                ('is_closed', models.BooleanField(db_column='is_closed', verbose_name='закрыт')),
                ('contractor', models.ForeignKey(db_column='contractor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'db_table': 'status_for_contractor',
                'verbose_name_plural': 'статусы задач для исполнителей',
                'verbose_name': 'статус задачи для исполнителя',
            },
        ),
        migrations.CreateModel(
            name='StatusForContractorInfo',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('status', models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, to='app.StatusForContractor', verbose_name='статус')),
            ],
            options={
                'db_table': 'status_for_contractor_info',
                'verbose_name_plural': 'строки истории статусов задач для исполнителей',
                'verbose_name': 'строка истории статусов задачи для исполнителя',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('title', models.CharField(db_column='title', max_length=100, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='описание')),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
                ('contractor', models.ForeignKey(db_column='contractor', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'db_table': 'task',
                'verbose_name_plural': 'задачи',
                'verbose_name': 'задача',
            },
        ),
        migrations.AddField(
            model_name='statusforcontractorinfo',
            name='task',
            field=models.ForeignKey(db_column='task', on_delete=django.db.models.deletion.CASCADE, to='app.Task', verbose_name='задача'),
        ),
        migrations.AddField(
            model_name='statusforclientinfo',
            name='task',
            field=models.ForeignKey(db_column='task', on_delete=django.db.models.deletion.CASCADE, to='app.Task', verbose_name='задача'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(db_column='task', on_delete=django.db.models.deletion.CASCADE, to='app.Task', verbose_name='задача'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]