from django.contrib.auth.admin import UserAdmin
from users.models import User
from django.contrib import admin
from django.contrib.auth.models import Group

# Unregister default group model
admin.site.unregister(Group)


@admin.register(User)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'fullname', 'country', 'date_joined', 'is_superuser', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'country', 'fullname')
    search_help_text = 'Search in Email, Country and Fullname'
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('is_superuser',)
    fieldsets = ()
