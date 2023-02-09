from django.contrib import admin
from snack.models import Snack
from user.models import User, EmailHistory


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'url', 'description', 'is_accepted', 'supply_year', 'supply_month']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ['email']
