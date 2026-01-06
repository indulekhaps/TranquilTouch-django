from django.db import models


# Create your models here.
class Appointmentdb(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    STAFF_LEVEL_CHOICES = (
        ('gold', 'Gold Level'),
        ('silver', 'Silver Level'),
        ('bronze', 'Bronze Level'),
    )
    Customer_name = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.CharField(max_length=10, blank=True, null=True)
    Category = models.CharField(max_length=100, blank=True, null=True)
    Service = models.CharField(max_length=100, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    staff_level = models.CharField(
        max_length=20,
        choices=STAFF_LEVEL_CHOICES
    )

    assigned_staff = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
