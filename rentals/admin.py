from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import rentals, RentalImage


class RentalImageAdmin(admin.StackedInline):
    model = RentalImage


@admin.register(rentals)
class rentalsAdmin(admin.ModelAdmin):
    inlines = [RentalImageAdmin]
    

    class Meta:
        model = rentals


@admin.register(RentalImage)
class RentalImageAdmin(admin.ModelAdmin):
    pass


