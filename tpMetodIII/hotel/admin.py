from django.contrib import admin

from .models import *
import os


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_number', 'client_name', 'client_lastname', 'client_email', 'get_ownership_rate',
                    'get_count_rentaldate', 'total', 'date', )

    def get_count_rentaldate(self, obj):
        return obj.rentaldate_set.count()
    get_count_rentaldate.short_description = 'Rental Date Quantity'
    get_count_rentaldate.admin_order_field = 'rentaldate__id'

    def get_ownership_rate(self, obj):
        return obj.rentaldate_set.all()[0].ownership.rate
    get_ownership_rate.short_description = 'Ownership Rate'
    get_ownership_rate.admin_order_field = 'rentaldate__ownership__rate'

    def get_queryset(self, request):
        if not request.user.is_superuser:
            return super(BookAdmin, self).get_queryset(request)\
                .filter(rentaldate__ownership__host__id=request.user.id)\
                .distinct()
        return super(BookAdmin, self).get_queryset(request)

    def delete_queryset(self, request, queryset):
        for book in queryset:
            rental_dates = RentalDate.objects.filter(booked=book)
            for rental_date in rental_dates:
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
            return super(OwnershipAdmin, self).get_queryset(request).filter(host=request.user)
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
