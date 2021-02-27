from django.contrib import admin
from .models import RequestsHelps


class RequestsHelpAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'publish', 'classes')
    list_filter = ('subject', 'publish')
    date_hierarchy = 'publish'


admin.site.register(RequestsHelps, RequestsHelpAdmin)