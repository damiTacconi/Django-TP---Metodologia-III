from django.contrib import admin

from .models import *
import os

class OwnershipAdmin(admin.ModelAdmin):
    exclude = ('host',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.host = Host.objects.get(pk=request.user.id)
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if os.path.isfile(str(obj.cover)):
                os.remove(str(obj.cover))
            obj.delete()

class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'password')


# Register your models here.
admin.site.register(City)
admin.site.register(Ownership, OwnershipAdmin)
admin.site.register(Book)
admin.site.register(Host, HostAdmin)
