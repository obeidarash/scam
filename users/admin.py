from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_superuser', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'country')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('is_superuser',)
    fieldsets = ()
    # autocomplete_fields = ('country',)
