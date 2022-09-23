from django.contrib import admin
from django.utils.html import format_html

from .models import Withdraw, Deposit
from .forms import DepositAdminForm, WithdrawAdminForm


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    form = DepositAdminForm
    list_display = ('user', 'tronscan', 'date', 'is_approved', 'is_decline')
    search_fields = ['hash', ]
    search_help_text = 'Search in Hash'
    sortable_by = ('-date',)
    list_filter = ('is_approved', 'is_decline',)
    readonly_fields = ('hash', 'user')

    def tronscan(self, obj):
        return format_html("<a href='https://tronscan.org/#/transaction/{}' target='_blank'>{}</a>", obj.hash, obj.hash)

    tronscan.allow_tags = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    form = WithdrawAdminForm
    list_display = ('user', 'date', 'is_decline', 'is_approved')
    search_fields = ['wallet_id', 'hash', ]
    search_help_text = 'Search in Wallet ID and HASH'
    sortable_by = ('-date',)
    list_filter = ('is_decline', 'is_approved',)
    readonly_fields = ('user', 'wallet_id',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
