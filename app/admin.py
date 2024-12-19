# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default User admin
admin.site.unregister(User)

# Optionally, you can create a custom admin for User if needed
class CustomUserAdmin(UserAdmin):
    model = User
    # Add any additional configuration for the admin interface here

# Register the User model with the custom admin
admin.site.register(User, CustomUserAdmin)


#### Razor pay:

from django.contrib import admin
from .models import Razorpay,Contactdetail,RecipientEmail


class RazorpayAdmin(admin.ModelAdmin):
   list_display = ('id','user','payment_id', 'order_id', 'signature', 'amount','status','created_at', )
admin.site.register(Razorpay, RazorpayAdmin)

#### admin for contact from

@admin.register(Contactdetail)
class ContactdetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'emailname', 'phonenumber', 'message']


@admin.register(RecipientEmail)
class RecipientEmailAdmin(admin.ModelAdmin):
    list_display = ['emailaddress']


#### realstate and homeproperty for admin 


from django.contrib import admin
from .models import RealEstateProperty

class RealEstatePropertyAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'location', 'property_type', 'created_at']
    search_fields = ['title', 'location']
    list_filter = ['property_type', 'created_at']

admin.site.register(RealEstateProperty, RealEstatePropertyAdmin)


from django.contrib import admin
from .models import Homeproperties

class HomepropertiesAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'location']
    search_fields = ['title', 'location']

admin.site.register(Homeproperties, HomepropertiesAdmin)


#### filled KYC details and bank details:

# from django.contrib import admin
# from .models import Kyc, BankDetails

# class BankDetailsInline(admin.TabularInline):
#     model = BankDetails
#     extra = 1  # Number of extra blank forms to display in the admin interface

# class KycAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer_name', 'aadhar_card_number', 'pan_number')  # Columns to display in the list view
#     search_fields = ('customer_name', 'aadhar_card_number', 'pan_number')  # Fields to enable search functionality
#     inlines = [BankDetailsInline]  # Inline display of related BankDetails in the KYC admin page

# class BankDetailsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'account_holder_name', 'bank_account_number', 'ifsc_code', 'branch_name', 'kyc')  # Display fields
#     search_fields = ('account_holder_name', 'bank_account_number', 'ifsc_code')  # Enable search functionality
#     list_filter = ('branch_name',)  # Add filtering by branch name

# # Register the models with the admin interface
# admin.site.register(Kyc, KycAdmin)
# admin.site.register(BankDetails, BankDetailsAdmin)
