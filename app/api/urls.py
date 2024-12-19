# from django.urls import path
# from .api_razorpay import RazorpayOrderAPIView, TransactionAPIView

# urlpatterns = [
#     path("order/create/", 
#         RazorpayOrderAPIView.as_view(), 
#         name="razorpay-create-order-api"
#     ),
#     path("order/complete/", 
#         TransactionAPIView.as_view(), 
#         name="razorpay-complete-order-api"
#     ),
# ]



###### without api using ;

from django.urls import path
from .api_razorpay import create_razorpay_order, verify_razorpay_payment

urlpatterns = [
    # Other URL patterns
    path('order/create/', create_razorpay_order, name='create_razorpay_order'),
    path('order/complete/', verify_razorpay_payment, name='verify_razorpay_payment'),
]
