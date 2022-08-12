from django.contrib import admin
from .models import AccessToken


@admin.register(AccessToken)
class DepositAdmin(admin.ModelAdmin):
    # todo: there is a problem with searching in the admin area
    list_display = ('access_token', 'representative', 'user', 'is_used')
    search_fields = ['representative', 'user', ]
    autocomplete_fields = ('representative', 'user',)
    sortable_by = ('-date',)
    # readonly_fields = ('access_token',)
