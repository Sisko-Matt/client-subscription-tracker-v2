from django.db import models
from django.core.validators import MinValueValidator

class Client (models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]

    name = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    business_name= models.CharField( max_length=50)

    status = models.CharField( 
        max_length=50,
        choices= STATUS_CHOICES,
        default= 'active'
    )

    def __str__(self):
        return self.name
    
class Subscription (models.Model):
    PAYMENT_STATUS = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ]

    client = models.ForeignKey( 
        Client, 
        on_delete=models.CASCADE,
        related_name='subscriptions'
        )
    
    start_date = models.DateField()
    expiry_date = models.DateField()
    amount_paid = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0)]
    )
    
    payment_status = models.CharField( 
        max_length=50,
        choices= PAYMENT_STATUS,
        default='unpaid'
        )
    
    notes = models.TextField( 
        blank= True,
        null= True
        )

    def __str__(self):
        return f"{self.client.name} Subscription"    