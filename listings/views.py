from django.shortcuts import render
import os
import requests
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment

CHAPA_URL = "https://api.chapa.co/v1/transaction/initialize"
CHAPA_SECRET = os.getenv("CHAPA_SECRET_KEY")

class InitiatePaymentView(APIView):
    def post(self, request):
        email = request.data.get("email")
        amount = request.data.get("amount")
        booking_reference = str(uuid.uuid4())

        data = {
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "first_name": "John",
            "last_name": "Doe",
            "tx_ref": booking_reference,
            "callback_url": "http://localhost:8000/api/verify-payment/",
            "return_url": "http://localhost:8000/payment-success/",
            "customization[title]": "Booking Payment",
        }

        headers = {
            "Authorization": f"Bearer {CHAPA_SECRET}"
        }

        chapa_response = requests.post(CHAPA_URL, headers=headers, json=data)
        chapa_data = chapa_response.json()

        if chapa_response.status_code == 200 and chapa_data["status"] == "success":
            checkout_url = chapa_data["data"]["checkout_url"]
            Payment.objects.create(
                booking_reference=booking_reference,
                amount=amount,
                email=email,
                transaction_id=chapa_data["data"]["tx_ref"],
                status="Pending"
            )
            return Response({"checkout_url": checkout_url}, status=200)
        else:
            return Response({"error": "Payment initiation failed"}, status=400)
