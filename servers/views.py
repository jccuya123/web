# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy

from servers.models import ServerModel
# Create your views here.

class ServerList(ListView):
	model = ServerModel

class ServerInsert(CreateView):
	model = ServerModel
	success_url = reverse_lazy('servers_list')
	fields = ['name', 'address', 'emailid']

class ServerUpdate(UpdateView):
	model = ServerModel
	success_url = reverse_lazy('servers_list')
	fields = ['name', 'address', 'emailid']

class ServerDelete(DeleteView):
	model = ServerModel
	success_url = reverse_lazy('servers_list')

