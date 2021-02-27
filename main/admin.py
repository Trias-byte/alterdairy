from django.contrib import admin
from .models import Peaples


class PeapleAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'secondName', 'thirdName', 'role', 'classes', 'rayon')
    list_filter = ('role', 'classes', 'rayon', 'firstName')
    search_fields = ('firstName',)


admin.site.register(Peaples, PeapleAdmin)