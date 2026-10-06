from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ElectricityBill
from .serializers import ElectricityBillSerializer

class CalculateBillView(APIView):
    def post(self, request):
        customer_name = request.data.get("customer_name")
        units = request.data.get("units")

        if not customer_name:
            return Response(
                {
                    "success": False,
                    "message": "Customer name is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if units is None or units == "":
            return Response(
                {
                    "success": False,
                    "message": "Units are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            units = Decimal(str(units))
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "Units must be a valid number."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if units < 0:
            return Response(
                {
                    "success": False,
                    "message": "Units cannot be negative."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

# ELECTRICITY SLAB CALCULATION

        energy_charge = Decimal("0.00")
        fixed_charge = Decimal("0.00")

        # 0 - 100 units
        if units <= 100:
            energy_charge = (units * Decimal("1.50"))
            fixed_charge = Decimal("50.00")

        # 101 - 200 units
        elif units <= 200:
            energy_charge = (Decimal("100") * Decimal("1.50")) + ((units - Decimal("100")) * Decimal("2.50"))
            fixed_charge = Decimal("75.00")

        # 201 - 500 units
        elif units <= 500:
            energy_charge = (Decimal("100") * Decimal("1.50")) + (Decimal("100") * Decimal("2.50")) + ((units - Decimal("200")) * Decimal("4.00"))
            fixed_charge = Decimal("100.00")

        # Above 500 units
        else:
            energy_charge = (Decimal("100") * Decimal("1.50")) + (Decimal("100") * Decimal("2.50")) + (Decimal("300") * Decimal("4.00")) + ((units - Decimal("500")) * Decimal("6.00"))
            fixed_charge = Decimal("150.00")

        # SUBTOTAL
        subtotal = (energy_charge + fixed_charge)
        
        # TAX - 5%
        tax = subtotal * Decimal("0.05")

        # TOTAL
        total_bill = subtotal + tax

        # USAGE MESSAGE
        if units <= 100:
            usage_message = "Low Usage"
        elif units <= 300:
            usage_message = "Normal Usage"
        else:
            usage_message = "High Usage"

        # SAVE TO DATABASE
        bill = ElectricityBill.objects.create(
            customer_name=customer_name.strip(),
            units=units,
            energy_charge=energy_charge,
            fixed_charge=fixed_charge,
            subtotal=subtotal,
            tax=tax,
            total_bill=total_bill,
            usage_message=usage_message,
        )
        
        # SERIALIZE RESPONSE
        serializer = ElectricityBillSerializer(bill)
        return Response(
            {
                "success": True,
                "message": "Bill calculated successfully.",
                "bill": serializer.data,
            },
            status=status.HTTP_201_CREATED
        )

class BillListView(APIView):
    def get(self, request):
        bills = ElectricityBill.objects.all().order_by("-created_at")
        serializer = ElectricityBillSerializer(bills, many=True)
        return Response(
            {
                "success": True,
                "count": bills.count(),
                "bills": serializer.data,
            }
        )