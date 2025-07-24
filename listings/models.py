from django.db import models

class Payment(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed"),
    )

    booking_reference = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking_reference} - {self.status}"
