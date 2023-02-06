from django.contrib import admin
from snack.models import Snack
from user.models import User, EmailHistory


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'url', 'description', 'state', 'arrive_month']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'password', 'is_admin']


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ['email']