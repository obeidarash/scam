from django.contrib import admin
from .models import AccessToken


@admin.register(AccessToken)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'representative', 'user', 'is_used', 'by_superuser')
    search_fields = ['access_token', ]
    search_help_text = 'Search in Tokens'
    autocomplete_fields = ('representative', 'user',)
    sortable_by = ('-date',)
    list_filter = ('by_superuser', 'is_used')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
