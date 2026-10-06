from django.db import models

class ElectricityBill(models.Model):
    customer_name = models.CharField(max_length=100)
    units = models.DecimalField(max_digits=10,decimal_places=2)
    energy_charge = models.DecimalField(max_digits=10,decimal_places=2)
    fixed_charge = models.DecimalField(max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    tax = models.DecimalField(max_digits=10,decimal_places=2)
    total_bill = models.DecimalField(max_digits=10,decimal_places=2)
    usage_message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.customer_name} - "
            f"{self.total_bill}"
        )


