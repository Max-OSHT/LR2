from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
# class UsersInline(admin.StackedInline):
#     model = Users
#     can_delete = False
#     verbose_name_plural = "myUsers"

# class UserAdmin(BaseUserAdmin):
#     inlines = [UsersInline]

# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(Users, UserAdmin)
admin.site.register(Logg)