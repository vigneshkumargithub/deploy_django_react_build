from django.db import models
from django.contrib.auth.models import User

class Razorpay(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('failed', 'Failed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", related_name="razorpay_transactions", null=True, blank=True)
    payment_id = models.CharField(max_length=200, verbose_name="Payment ID")
    order_id = models.CharField(max_length=200, verbose_name="Order ID")
    signature = models.CharField(max_length=500, verbose_name="Signature", blank=True, null=True)
    amount = models.IntegerField(verbose_name="Amount")
    currency = models.CharField(max_length=10, verbose_name="Currency", default='INR')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
         return f"{self.user.username if self.user else 'No User'} - {self.id}"


##### contact form model

from django.db import models
from django.core.validators import RegexValidator
import uuid    

class RecipientEmail(models.Model):
    emailaddress = models.EmailField(unique=True)

class Contactdetail(models.Model):
    name = models.CharField(max_length=100)
    emailname = models.EmailField(unique=True,default="")
    phonenumber = models.CharField(max_length=15,
        validators=[
            RegexValidator(
                regex=r'^[0-9]+$', 
                message='Phone number must only contain numeric values.',
                code='invalid_phonenumber',
            )
        ],default=""
    )
    message = models.TextField(default="")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact detail"


#### models for home property  and realstate property

from django.db import models

class RealEstateProperty(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    property_type = models.CharField(max_length=100, choices=[('residential', 'Residential'), ('commercial', 'Commercial')])
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Realstate_Property"


from django.db import models

class Homeproperties(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Home_property"



##### filled kyc details and bank details

# from django.db import models

# class Kyc(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kycs", null=True, blank=True)
#     customer_name = models.CharField(max_length=100)
#     aadhar_card_number = models.CharField(max_length=12, unique=True)
#     pan_number = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.customer_name


# class BankDetails(models.Model):
#     kyc = models.ForeignKey(Kyc, on_delete=models.CASCADE, related_name='bank_details')
#     account_holder_name = models.CharField(max_length=100)
#     bank_account_number = models.CharField(max_length=20, unique=True)
#     ifsc_code = models.CharField(max_length=11)
#     branch_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.account_holder_name

