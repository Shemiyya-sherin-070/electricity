from django.contrib import admin
from .models import ElectricityBill

@admin.register(ElectricityBill)
class ElectricityBillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "units",
        "total_bill",
        "usage_message",
        "created_at",
    )
    list_filter = (
        "usage_message",
        "created_at",
    )
    search_fields = (
        "customer_name",
    )
    