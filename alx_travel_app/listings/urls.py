from django.urls import path
from .views import InitiatePaymentView, VerifyPaymentView

urlpatterns = [
    path("initiate-payment/", InitiatePaymentView.as_view(), name="initiate-payment"),
    path("verify-payment/", VerifyPaymentView.as_view(), name="verify-payment"),
]
