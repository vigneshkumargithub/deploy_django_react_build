from django.urls import path
from . views import *
from . import views 
from .views import RealEstatePropertyViewSet, HomepropertiesViewset


urlpatterns = [
    #####*****************************####
    ## authenication ==> working perfectly authentication frontend and backend with API using this urls

    # path('signupdata/', RegisterView.as_view(), name='signup'),
    # path('logindata/', LoginView.as_view(), name='login'),
    # path('resetpassworddata/', ResetPasswordView.as_view(), name='reset_password'),
    # path('forgotpassworddata/', ForgotPasswordView.as_view(), name='forgot_password'),
    # path('resetpasswordconfirmdata/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),


  #####*****************************####
  ## authenication ==> working perfectly authentication frontend and backend without API using this urls

    path('signupdata/', views.register_user, name='signup'),
    path('logindata/', views.login_user, name='login'),
    path('resetpassworddata/', views.reset_password, name='reset_password'),
    path('forgotpassworddata/', views.forgot_password, name='forgot_password'),
    path('resetpasswordconfirmdata/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),

    #### url for contact form
    path('contactformdata/', ContactForm.as_view(), name='submit-form'),


    ##### realstate and homeproperty for urls
    # path("homeproperties/", HomepropertiesViewset.as_view, name="homeproperties"),
    # path("homeproperties/", RealEstatePropertyViewSet.as_view, name="Realestateproperty")

    path("propertiesdata/", HomepropertiesViewset.as_view({'get': 'list', 'post': 'create'}), name="homeproperties"),
    path("homepropertiesdata/", RealEstatePropertyViewSet.as_view({'get': 'list', 'post': 'create'}), name="realestateproperty"),

    # #### filled kyc details and bank details
    # # KYC URLs
    # path('api/kyc/', KycViewSet.as_view({'get': 'list', 'post': 'create'}), name='kyc-list-create'),
    # path('api/kyc/<int:pk>/', KycViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='kyc-detail'),

    # # Bank Details URLs
    # path('api/bankdetails/', BankDetailsViewSet.as_view({'get': 'list', 'post': 'create'}), name='bankdetails-list-create'),
    # path('api/bankdetails/<int:pk>/', BankDetailsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bankdetails-detail'),

    path("", index, name="index")
] 