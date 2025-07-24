from django.shortcuts import render
import os
import uuid
import requests
from django.shortcuts import redirect
from django.http import JsonResponse

def initiate_payment(request):
    chapa_url = "https://api.chapa.co/v1/transaction/initialize"
    CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")

    data = {
        "amount": "100",
        "currency": "ETB",
        "email": "brendabjematia@gmail.com.com",
        "first_name": "Brenda",
        "last_name": "Bonareri",
        "tx_ref": str(uuid.uuid4()),
        "callback_url": "http://localhost:8000/payments/callback/",
        "return_url": "http://localhost:8000/payments/success/",
        "customization[title]": "Travel App Payment",
        "customization[description]": "Payment for a travel package"
    }

    headers = {
        "Authorization": f"Bearer {CHAPA_SECRET_KEY}"
    }

    response = requests.post(chapa_url, json=data, headers=headers)
    result = response.json()

    if result.get("status") == "success":
        return redirect(result["data"]["checkout_url"])
    else:
        return JsonResponse(result)

