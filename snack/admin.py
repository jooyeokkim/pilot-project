from django.contrib import admin
from snack.models import Snack, SnackRequest
from user.models import User


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'url']
    fields = ['name', 'image', 'url']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']
    fields = ['email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']

@admin.register(SnackRequest)
class SnackRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'snack', 'description', 'is_accepted', 'supply_year', 'supply_month']
    fields = ['snack', 'description', 'is_accepted', 'supply_year', 'supply_month']
