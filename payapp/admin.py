from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'amount', 'transaction_type', 'status', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Transaction, TransactionAdmin)
