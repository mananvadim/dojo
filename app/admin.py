# -*- coding: utf-8 -*-


from django.contrib import admin
from app.models import *


class BaseModelAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'version',
        'creation_date',
    )
    readonly_fields = (
        'id',
        'version',
        'creation_date',
    )
    list_display = (
        'id',
        'version',
        'creation_date',
    )


class ContractAdmin(BaseModelAdmin):
    own_fields = (
        'author',
        'client',
        'contractor',
        'is_active',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectAdmin(BaseModelAdmin):
    own_fields = (
        'name',
        'client',
        'contractor',
        'description',
        'status_for_client',
        'status_for_contractor',
        'status_date_for_client',
        'status_date_for_contractor',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectCommentAdmin(BaseModelAdmin):
    own_fields = (
        'project',
        'task',
        'user',
        'text',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectStatusForClientAdmin(BaseModelAdmin):
    own_fields = (
        'name',
        'client',
        'is_closed',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectStatusForContractorAdmin(BaseModelAdmin):
    own_fields = (
        'name',
        'contractor',
        'is_closed',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectStatusInfoForClientAdmin(BaseModelAdmin):
    own_fields = (
        'project',
        'status',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class ProjectStatusInfoForContractorAdmin(BaseModelAdmin):
    own_fields = (
        'project',
        'status',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class TaskAdmin(BaseModelAdmin):
    own_fields = (
        'name',
        'project',
        'description',
        'status',
        'status_date',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class TaskWorkAdmin(BaseModelAdmin):
    own_fields = (
        'task',
        'date',
        'work',
        'comment',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class TaskStatusAdmin(BaseModelAdmin):
    own_fields = (
        'name',
        'contractor',
        'is_closed',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class TaskStatusInfoAdmin(BaseModelAdmin):
    own_fields = (
        'task',
        'status',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


class UserSettingAdmin(BaseModelAdmin):
    own_fields = (
        'user',
        'new_project_status_for_client',
        'new_project_status_for_contractor',
        'new_task_status',
    )
    fields = BaseModelAdmin.fields + own_fields
    list_display = BaseModelAdmin.list_display + own_fields


admin.site.register(Contract, ContractAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectComment, ProjectCommentAdmin)
admin.site.register(ProjectStatusForClient, ProjectStatusForClientAdmin)
admin.site.register(ProjectStatusForContractor, ProjectStatusForContractorAdmin)
admin.site.register(ProjectStatusInfoForClient, ProjectStatusInfoForClientAdmin)
admin.site.register(ProjectStatusInfoForContractor, ProjectStatusInfoForContractorAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskWork, TaskWorkAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(TaskStatusInfo, TaskStatusInfoAdmin)
admin.site.register(UserSetting, UserSettingAdmin)