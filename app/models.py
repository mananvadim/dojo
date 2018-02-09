# -*- coding: utf-8 -*-


import uuid
from django.db import models, connection
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(
        db_column='id',
        primary_key=True,
    )
    version = models.UUIDField(
        db_column='version',
        null=True,
    )
    creation_date = models.DateTimeField(
        db_column='creation_date',
        auto_now_add=True,
    )

    class Meta:
        abstract = True

    def changed_deleted(self):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT version FROM " + self._meta.db_table + " WHERE id = ? FOR UPDATE",
            [self.id]
        )
        row = cursor.fetchone()
        if row == None:
            return('does not exist')
        elif not row[0] == self.version:
            return ('is changed')
        else:
            return ('ok')

    def save(self, *args, **kwargs):
        if self.id == None:
            self.id = uuid.uuid4()
        else:
            pass
            #result = self.changed_deleted()
            #if not result == 'ok':
            #   raise Exception(result)
        self.version = uuid.uuid4()
        super(BaseModel, self).save(*args, **kwargs) # Call the "real" save() method.
        #do_something_else()

    def delete(self, *args, **kwargs):
        if self.id == None:
            raise Exception('deleting whith id==None')
        else:
            pass
            #result = self.changed_deleted()
            #if not result == 'ok':
            #   raise Exception(result)
        super(BaseModel, self).delete(*args, **kwargs) # Call the "real" delete() method.
        #do_something_else()


class Contract(BaseModel):
    author = models.ForeignKey(
        User,
        db_column='author',
        verbose_name='инициатор',
        related_name='+',
    )
    client = models.ForeignKey(
        User,
        db_column='client',
        verbose_name='заказчик',
        related_name='+',
    )
    contractor = models.ForeignKey(
        User,
        db_column='contractor',
        verbose_name='исполнитель',
        related_name='+',
    )
    is_active = models.BooleanField(
        db_column='is_active',
        default=False,
        verbose_name ='это действующий договор',
    )

    class Meta:
        db_table = 'contract'
        unique_together = (
            'client',
            'contractor'
        )
        verbose_name = 'договор'
        verbose_name_plural = 'договоры'

    def __str__(self):
        client_name = self.client.last_name + ' ' + self.client.first_name
        contractor_name = self.contractor.last_name + ' '+ self.contractor.first_name
        return client_name + '/'+ contractor_name


class Project(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='наименование',
    )
    client = models.ForeignKey(
        User,
        db_column='client',
        verbose_name='заказчик',
        related_name='+',
    )
    contractor = models.ForeignKey(
        User,
        db_column='contractor',
        verbose_name='исполнитель',
        related_name='+',
    )
    description = models.TextField(
        'описание',
        db_column='description',
    )
    status_for_client = models.ForeignKey(
        'ProjectStatusForClient',
        db_column='status_for_client',
        null=True,
        verbose_name='статус, установленный заказчиком',
    )
    status_for_contractor = models.ForeignKey(
        'ProjectStatusForContractor',
        db_column='status_for_contractor',
        null=True,
        verbose_name='статус, установленный исполнителем',
    )
    status_date_for_client = models.DateTimeField(
        db_column='status_date_for_client',
        null=True,
        verbose_name='дата статуса, установленного заказчиком',
    )
    status_date_for_contractor = models.DateTimeField(
        db_column='status_date_for_contractor',
        null=True,
        verbose_name='дата статуса, установленного исполнителем',
    )

    class Meta:
        db_table = 'project'
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self):
        return str(self.client)+' | '+str(self.contractor)+' | ' + str(self.name)


class ProjectComment(BaseModel):
    project = models.ForeignKey(
        'Project',
        db_column='project',
        verbose_name='проект',
    )
    task = models.ForeignKey(
        'Task',
        db_column='task',
        null=True,
        verbose_name='задача',
    )
    user = models.ForeignKey(
        User,
        db_column='user',
        verbose_name='пользователь',
    )
    text = models.TextField(
        'текст комментария',
        db_column='text',
    )

    class Meta:
        db_table = 'project_comment'
        verbose_name = 'комментарий к проекту'
        verbose_name_plural = 'комментарии к проектам'

    def __str__(self):
        return str(self.text)


class ProjectStatusForClient(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='наименование',
    )
    client = models.ForeignKey(
        User,
        db_column='client',
        verbose_name='заказчик',
    )
    is_closed = models.BooleanField(
        db_column='is_closed',
        verbose_name ='это закрывающий проект статус',
    )

    class Meta:
        db_table = 'project_status_for_client'
        verbose_name = 'статус проекта для заказчика'
        verbose_name_plural = 'статусы проектов для заказчиков'

    def __str__(self):
        return str(self.name)


class ProjectStatusForContractor(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='наименование',
    )
    contractor = models.ForeignKey(
        User,
        db_column='contractor',
        verbose_name='исполнитель',
    )
    is_closed = models.BooleanField(
        db_column='is_closed',
        verbose_name ='это закрывающий проект статус',
    )

    class Meta:
        db_table = 'project_status_for_contractor'
        verbose_name = 'статус проекта для исполнителя'
        verbose_name_plural = 'статусы проектов для исполнителей'

    def __str__(self):
        return str(self.name)


class ProjectStatusInfoForClient(BaseModel):
    project = models.ForeignKey(
        'Project',
        db_column='project',
        verbose_name='проект',
    )
    status = models.ForeignKey(
        'ProjectStatusForClient',
        db_column='status',
        verbose_name='статус',
    )

    class Meta:
        db_table = 'project_status_info_for_client'
        verbose_name = 'строка истории статусов проекта для заказчика'
        verbose_name_plural = 'строки истории статусов проектов для заказчиков'

    def __str__(self):
        return str(self.id)


class ProjectStatusInfoForContractor(BaseModel):
    project = models.ForeignKey(
        'Project',
        db_column='project',
        verbose_name='проект',
    )
    status = models.ForeignKey(
        'ProjectStatusForContractor',
        db_column='status',
        verbose_name='статус',
    )

    class Meta:
        db_table = 'project_status_info_for_contractor'
        verbose_name = 'строка истории статусов проекта для исполнителя'
        verbose_name_plural = 'строки истории статусов проектов для исполнителей'

    def __str__(self):
        return str(self.id)


class Task(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='наименование',
    )
    project = models.ForeignKey(
        'Project',
        db_column='project',
        verbose_name='проект',
    )
    description = models.TextField(
        'описание',
        db_column='description',
    )
    status = models.ForeignKey(
        'TaskStatus',
        db_column='status',
        null=True,
        verbose_name='статус',
    )
    status_date = models.DateTimeField(
        db_column='status_date',
        null=True,
        verbose_name='дата статуса',
    )

    class Meta:
        db_table = 'task'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return str(self.name)


class TaskWork(BaseModel):
    task = models.ForeignKey(
        'Task',
        db_column='task',
        verbose_name='задача',
    )
    date = models.DateField(
        db_column='date',
        verbose_name='дата работ',
    )
    work = models.PositiveIntegerField(
        db_column='work',
        verbose_name='количество часов',
    )
    comment = models.TextField(
        'комментарий',
        db_column='comment',
    )

    class Meta:
        db_table = 'task_work'
        verbose_name = 'работы по задаче'
        verbose_name_plural = 'работы по задачам'

    def __str__(self):
        return str(self.comment)


class TaskStatus(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='наименование',
    )
    contractor = models.ForeignKey(
        User,
        db_column='contractor',
        verbose_name='исполнитель',
    )
    is_closed = models.BooleanField(
        db_column='is_closed',
        verbose_name ='это закрывающий задачу статус',
    )

    class Meta:
        db_table = 'task_status'
        verbose_name = 'статус задачи'
        verbose_name_plural = 'статусы задач'

    def __str__(self):
        return str(self.name)


class TaskStatusInfo(BaseModel):
    task = models.ForeignKey(
        'Task',
        db_column='task',
        verbose_name='задача',
    )
    status = models.ForeignKey(
        'TaskStatus',
        db_column='status',
        verbose_name='статус',
    )

    class Meta:
        db_table = 'task_status_info'
        verbose_name = 'строка истории статусов задачи'
        verbose_name_plural = 'строки истории статусов задач'

    def __str__(self):
        return str(self.id)


class UserSetting(BaseModel):
    user = models.OneToOneField(
        User,
        db_column='user',
        verbose_name='пользователь',
    )
    new_project_status_for_client = models.ForeignKey(
        'ProjectStatusForClient',
        db_column='new_project_status_for_client',
        null=True,
        verbose_name='статус нового проекта для заказчика',
    )
    new_project_status_for_contractor = models.ForeignKey(
        'ProjectStatusForContractor',
        db_column='new_project_status_for_contractor',
        null=True,
        verbose_name='статус нового проекта для исполнителя',
    )
    new_task_status = models.ForeignKey(
        'TaskStatus',
        db_column='new_task_status',
        null=True,
        verbose_name='статус новой задачи',
    )

    class Meta:
        db_table = 'user_setting'
        verbose_name = 'настройка пользователя'
        verbose_name_plural = 'настройки пользователей'

    def __str__(self):
        return str(self.id)

