from django.urls import path
from .views import (CalculateBillView, BillListView)

urlpatterns = [
    path("calculate-bill/", CalculateBillView.as_view(), name="calculate-bill"),
    path("bills/", BillListView.as_view(), name="bill-list"),
]