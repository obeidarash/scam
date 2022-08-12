from django.contrib import admin
from .models import Withdraw, Deposit
from .forms import DepositAdminForm


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    form = DepositAdminForm
    list_display = ('user', 'date', 'is_approved', 'is_decline')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    sortable_by = ('-date',)

    # readonly_fields = ('hash', 'user')

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    readonly_fields = ('user',)
    sortable_by = ('-date',)
