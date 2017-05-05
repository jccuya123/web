# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import decimal, csv

from django.contrib import admin
from django.http import HttpResponse
from django.db.models import F
from .models import ServerModel

# Register your models here.

def export_server(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachement; filename="file.csv"'
	writer = csv.writer(response)
	write.writer(['Name', 'Address', 'Email ID'])
	server_file = queryset.values_list('name', 'address', 'emailid')
	for servermodel in server_file:
		writer.writerow(servermodel)
	return response
export_server.short_description = 'Export to csv'

class ServerAdmin(admin.ModelAdmin):
	pass

admin.site.register(ServerModel)