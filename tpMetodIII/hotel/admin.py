from django.contrib import admin

from .models import *

class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'password')
# Register your models here.
admin.site.register(City)
admin.site.register(Ownership)
admin.site.register(Book)
admin.site.register(Host,HostAdmin)
