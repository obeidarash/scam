from django.contrib import admin
from .models import Withdraw, Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'is_approved', 'is_decline')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    # readonly_fields = ('hash', 'user')


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    search_fields = ['user', ]
    autocomplete_fields = ('user',)
    readonly_fields = ('user',)
