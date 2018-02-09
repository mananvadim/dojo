# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.forms.models import model_to_dict
from jsonrpc import jsonrpc_method
from app.models import *


def cigar_wish_list(request):
    return HttpResponse('test')


def index(request):
    return render(request, 'app/base.html')


@jsonrpc_method('app.authenticated', authenticated=True)
def authenticated(request):
    return True


@jsonrpc_method('app.add_contract_whith_client', authenticated=True)
@transaction.atomic
def add_contract_whith_client(request, client_id):
    client = User.objects.get(id=client_id)

    contract = Contract()
    contract.author = request.user
    contract.client = client
    contract.contractor = contract.author
    contract.is_active = False
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


@jsonrpc_method('app.activate_contract_whith_contractor', authenticated=True)
@transaction.atomic
def activate_contract_whith_contractor(request, contractor_id):
    contractor = User.objects.get(id=contractor_id)

    contract = Contract.objects.get(
        ~Q(author=request.user),
        Q(client=request.user),
        Q(contractor=contractor),
        Q(is_active=False)
    )
    contract.is_active = True
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


@jsonrpc_method('app.deactivate_contract_whith_contractor', authenticated=True)
@transaction.atomic
def deactivate_contract_whith_contractor(request, contractor_id):
    contractor = User.objects.get(id=contractor_id)

    contract = Contract.objects.get(
        ~Q(author=request.user),
        Q(client=request.user),
        Q(contractor=contractor),
        Q(is_active=True)
    )
    contract.is_active = False
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


@jsonrpc_method('app.add_contract_whith_contractor', authenticated=True)
@transaction.atomic
def add_contract_whith_contractor(request, contractor_id):
    contractor = User.objects.get(id=contractor_id)

    contract = Contract()
    contract.author = request.user
    contract.client = contract.author
    contract.contractor = contractor
    contract.is_active = False
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


@jsonrpc_method('app.activate_contract_whith_client', authenticated=True)
@transaction.atomic
def activate_contract_whith_client(request, client_id):
    client = User.objects.get(id=client_id)

    contract = Contract.objects.get(
        ~Q(author=request.user),
        Q(client=client),
        Q(contractor=request.user),
        Q(is_active=False)
    )
    contract.is_active = True
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


@jsonrpc_method('app.deactivate_contract_whith_client', authenticated=True)
@transaction.atomic
def deactivate_contract_whith_client(request, client_id):
    client = User.objects.get(id=client_id)

    contract = Contract.objects.get(
        ~Q(author=request.user),
        Q(client=client),
        Q(contractor=request.user),
        Q(is_active=True)
    )
    contract.is_active = False
    contract.save()
    return model_to_dict(Contract.objects.get(id=contract.id))


"""
@jsonrpc_method('app.create_contract_by_contractor_for_activate', authenticated=True)
def create_contract_by_contractor_for_activate(request, client_id):
    try:
        client = User.objects.get(id=client_id)
    except:
        return 'No client whith client_id=' + str(contractor_id)
    contract = Contract()
    contract.name = 'main'
    contract.author = request.user
    contract.contractor = contract.author
    contract.client = client
    contract.is_active = False
    contract.save()
    return contract.id


@jsonrpc_method('app.activate_contract_by_client', authenticated=True)
def activate_contract_by_client(request, client_id):


@jsonrpc_method('app.get_clients', authenticated=True)
def get_clients(request):
    contracts = Contract.objects.filter(contractor=request.user)

    clients = []
    for contract in contracts:
        client = {}
        client['id'] = contract.client.id
        client['first_name'] = contract.client.first_name
        client['last_name'] = contract.client.last_name
        clients.append(client)
    return clients
"""

"""
@jsonrpc_method('app.get_task_list', authenticated=True)
def get_task_list(request):

    tasks = Task.objects.all()
    lst = []
    for task in tasks:
        tsk = {}
        tsk['id'] = task.id
        tsk['title'] = task.title

        client = {}
        client['id'] = task.client.id
        client['first_name'] = task.client.first_name
        client['last_name'] = task.client.last_name
        tsk['client'] = client

        contractor = {}
        contractor['id'] = task.contractor.id
        contractor['first_name'] = task.contractor.first_name
        contractor['last_name'] = task.contractor.last_name
        tsk['contractor'] = contractor

        tsk['creation_date'] = task.creation_date
        tsk['text'] = task.text
        lst.append(tsk)

    return lst


@jsonrpc_method('app.get_task_with_comments', authenticated=True)
def get_task_with_comments(request, task_id):

    task = Task.objects.get(id=task_id)
    tsk = {}
    tsk['id'] = task.id
    tsk['title'] = task.title

    client = {}
    client['id'] = task.client.id
    client['first_name'] = task.client.first_name
    client['last_name'] = task.client.last_name
    tsk['client'] = client

    contractor = {}
    contractor['id'] = task.contractor.id
    contractor['first_name'] = task.contractor.first_name
    contractor['last_name'] = task.contractor.last_name
    tsk['contractor'] = contractor

    tsk['creation_date'] = task.creation_date
    tsk['text'] = task.text

    comments = Comment.objects.filter(task=task)
    lst = []
    for comment in comments:
        cmnt = {}
        cmnt['creation_date'] = comment.creation_date
        cmnt['text'] = comment.text

        user = {}
        user['id'] = comment.user.id
        user['first_name'] = comment.user.first_name
        user['last_name'] = comment.user.last_name

        cmnt['user'] = user
        lst.append(cmnt)

    tsk['comments'] = lst
    return tsk


@jsonrpc_method('app.create_task', authenticated=True)
def create_task(request, title, text, contractor_id):

    task = Task()
    task.title = title
    task.text = text
    task.client = request.user

    contractor = User.objects.get(id=contractor_id)
    task.contractor = contractor
    task.save()
    return task.id



@jsonrpc_method('app.create_comment', authenticated=True)
def create_comment(request, task_id, text):

    task = Task.objects.get(id=task_id)

    comment = Comment()
    comment.task = task
    comment.user = request.user
    comment.text = text
    comment.save()
    return comment.id


"""
