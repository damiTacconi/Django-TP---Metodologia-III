from django.contrib import admin

from .models import *
import os


class BookAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if not request.user.is_superuser:
            pass
        return super(BookAdmin, self).get_queryset(request)

    def delete_queryset(self, request, queryset):
        for book in queryset:
            rental_date = RentalDate.objects.get(booked=book)
            rental_date.booked = None
            rental_date.save()
            book.delete()


class RentalDateInline(admin.TabularInline):
    model = RentalDate
    fk_name = 'ownership'
    max_num = 7


class OwnershipAdmin(admin.ModelAdmin):
    inlines = [RentalDateInline]
    list_display = ('title', 'city', 'host')
    exclude = ('host',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.host = Host.objects.get(pk=request.user.id)
        obj.save()

    def get_queryset(self, request):
        if not request.user.is_superuser:
            qs = super(OwnershipAdmin, self).get_queryset(request)
            return qs.filter(host=request.user)
        return super(OwnershipAdmin, self).get_queryset(request)

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
admin.site.register(Book, BookAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(RentalDate)
