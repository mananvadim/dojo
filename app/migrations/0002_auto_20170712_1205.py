# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 12:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('version', models.UUIDField(db_column='version')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creation_date', verbose_name='дата создания')),
                ('new_task_status_for_client', models.ForeignKey(db_column='new_task_status_for_client', on_delete=django.db.models.deletion.CASCADE, to='app.StatusForClient', verbose_name='статус новой задачи для заказчика')),
                ('new_task_status_for_contractor', models.ForeignKey(db_column='new_task_status_for_contractor', on_delete=django.db.models.deletion.CASCADE, to='app.StatusForContractor', verbose_name='статус новой задачи для исполнителя')),
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'настройка пользователя',
                'verbose_name_plural': 'настройки пользователей',
                'db_table': 'user_setting',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(db_column='text', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(db_column='title', max_length=100, verbose_name='тема'),
        ),
    ]
