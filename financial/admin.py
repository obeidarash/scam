from django.contrib import admin
from .models import Withdraw, Deposit
from .forms import DepositAdminForm, WithdrawAdminForm


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    form = DepositAdminForm
    list_display = ('user', 'hash', 'date', 'is_approved', 'is_decline')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    sortable_by = ('-date',)
    list_filter = ('is_approved', 'is_decline',)
    readonly_fields = ('hash', 'user')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    form = WithdrawAdminForm
    list_display = ('user', 'date', 'is_decline', 'is_approved')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    sortable_by = ('-date',)
    list_filter = ('is_decline', 'is_approved',)
    readonly_fields = ('user', 'wallet_id',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
