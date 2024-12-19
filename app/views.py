# # accounts/views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
# from .serializers import UserSerializer, LoginSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.core.mail import send_mail
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings
# from django.contrib.auth import authenticate
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.core.mail import send_mail
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings

######################## working perfectly authentication frontend and backend with API using

# # accounts/views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from .serializers import UserSerializer, LoginSerializer
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.core.mail import send_mail
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.conf import settings
# from django.contrib.auth import authenticate


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class ResetPasswordView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         confirm_password = request.data.get('confirm_password')

#         # Authenticate user
#         user = authenticate(username=username, password=old_password)
        
#         if user is not None:
#             if new_password == confirm_password:
#                 user.set_password(new_password)
#                 user.save()
#                 return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'New password and confirm password do not match'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'message': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)


# class ForgotPasswordView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'message': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#         token_generator = PasswordResetTokenGenerator()
#         token = token_generator.make_token(user)
#         uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

#         # reset_url = f"http://localhost:3001/resetpasswordconfirm/{uidb64}/{token}/"
#         reset_url = f"http://localhost:3000/resetpasswordconfirm/{uidb64}/{token}/"

#         # Send email
#         send_mail(
#             subject='Password Reset Request',
#             message=f'Click the link to reset your password: {reset_url}',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[email],
#         )

#         return Response({'message': 'Password reset link sent successfully check your email'}, status=status.HTTP_200_OK)


# class ResetPasswordConfirmView(APIView):
#     def post(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             return Response({'message': 'Invalid token or user ID'}, status=status.HTTP_400_BAD_REQUEST)
        
#         token_generator = PasswordResetTokenGenerator()
#         if not token_generator.check_token(user, token):
#             return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

#         new_password = request.data.get('new_password')
#         confirm_password = request.data.get('confirm_password')

#         if new_password != confirm_password:
#             return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user.set_password(new_password)
#         user.save()

#         return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

###************************************************************************###
###************************************************************************###

#### working perfectly authentication frontend and backend without API using


from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.authtoken.models import Token
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already taken'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        # Generate token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({'message': 'User registered successfully', 'token': token.key}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        # Authenticate by username or email
        user = authenticate(request, username=username_or_email, password=password)
        if not user:
            try:
                user_with_email = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_with_email.username, password=password)
            except User.DoesNotExist:
                pass

        if user:
            # Generate or retrieve the token for the user
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'message': 'Login successful', 'token': token.key}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        user = authenticate(request, username=username, password=old_password)
        if user:
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return JsonResponse({'message': 'Password updated successfully'}, status=200)
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        return JsonResponse({'error': 'Invalid old password'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist'}, status=404)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f"http://localhost:3000/resetpasswordconfirm/{uidb64}/{token}/"

        send_mail(
            subject='Password Reset Request',
            message=f'Click the link to reset your password: {reset_url}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        return JsonResponse({'message': 'Password reset link sent successfully. Check your email.'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def reset_password_confirm(request, uidb64, token):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return JsonResponse({'error': 'Invalid token or user ID'}, status=400)

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return JsonResponse({'error': 'Invalid or expired token'}, status=400)

        if new_password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        user.set_password(new_password)
        user.save()
        return JsonResponse({'message': 'Password reset successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)




###### views.py for contact from


from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contactdetail, RecipientEmail
from .serializers import ContactdetailSerializer
import re
from django.core.mail import send_mail
from django.conf import settings

# @method_decorator(csrf_exempt, name='dispatch')
class ContactForm(APIView):
    def post(self, request, *args, **kwargs):
        # Check for existing email ID and phone number
        existing_email = request.data.get('emailname')
        existing_phone = request.data.get('phonenumber')
        if Contactdetail.objects.filter(emailname=existing_email).exists():
            return Response({'detail': 'The email ID is already stored.'}, status=status.HTTP_400_BAD_REQUEST)
        if Contactdetail.objects.filter(phonenumber=existing_phone).exists():
            return Response({'detail': 'The phone number is already stored.'}, status=status.HTTP_400_BAD_REQUEST)
 
        # Validate phone number for non-numeric characters
        phone_number = request.data.get('phonenumber')
        if not re.match("^[0-9()#&+*-=.]+$", phone_number):
            return Response({'detail': 'Phone number must only contain numeric values.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactdetailSerializer(data=request.data)
        if serializer.is_valid():
            # Save contact form data
            serializer.save()

            # Fetch the recipient email address dynamically
            recipient_email_object = RecipientEmail.objects.first()
            if recipient_email_object:
                recipient_email_address = recipient_email_object.emailaddress

                # Send email to the recipient specified in the model
                send_mail(
                    'New Contact Form Submissions',
                    '',
                    settings.EMAIL_HOST_USER,  # Replace with your Gmail address
                    [recipient_email_address],  # Use the recipient_email from the model
                    fail_silently=False,
                    html_message=f'<b>Name:</b> {serializer.data["name"]}<br>'
                                  f'<b>EmailID:</b>  {serializer.data["emailname"]}<br>'
                                  f'<b>Phone:</b> {serializer.data["phonenumber"]}<br>'
                                  f'<b>Message:</b> {serializer.data["message"]}'
                )

            return Response({'detail': 'Thank you, our team will contact you.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######## realstate and homeproperties for views function


from rest_framework import viewsets
from .models import RealEstateProperty
from .serializers import RealEstatePropertySerializer

class RealEstatePropertyViewSet(viewsets.ModelViewSet):
    queryset = RealEstateProperty.objects.all()
    serializer_class = RealEstatePropertySerializer


# home page home property

from rest_framework import viewsets
from .models import Homeproperties
from .serializers import HomepropertiesSerializer

class HomepropertiesViewset(viewsets.ModelViewSet):
    queryset = Homeproperties.objects.all()
    serializer_class = HomepropertiesSerializer


#### filled bank details and bank details

# from rest_framework import viewsets
# from .models import Kyc, BankDetails
# from .serializers import KycSerializer, BankDetailsSerializer

# class KycViewSet(viewsets.ModelViewSet):
#     queryset = Kyc.objects.all()
#     serializer_class = KycSerializer

# class BankDetailsViewSet(viewsets.ModelViewSet):
#     queryset = BankDetails.objects.all()
#     serializer_class = BankDetailsSerializer


def index(request):
    return render (request,"index.html")