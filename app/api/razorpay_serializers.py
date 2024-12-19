# from rest_framework import serializers
# from ..models import Razorpay


# class RazorpayOrderSerializer(serializers.Serializer):
#     amount = serializers.IntegerField()
#     currency = serializers.CharField()


# class TranscationModelSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Razorpay
#         fields = ["payment_id", "order_id", "signature", "amount","currency", "status"]



################################################################################################################

####### working good condition :::
##### keela ulla function working good condition because login pana username oda
##### admin panel la store agum..


from rest_framework import serializers
from ..models import Razorpay
from django.contrib.auth.models import User


class RazorpayOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()


class TranscationModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Razorpay
        fields = ["user", "payment_id", "order_id", "signature", "amount", "currency", "status"]





# from rest_framework import serializers
# from ..models import Razorpay


# class RazorpayOrderSerializer(serializers.Serializer):
#     amount = serializers.IntegerField(required=True)
#     currency = serializers.CharField(max_length=10, default='INR')


# class TransactionSerializer(serializers.Serializer):
#     payment_id = serializers.CharField(max_length=200, required=True)
#     order_id = serializers.CharField(max_length=200, required=True)
#     signature = serializers.CharField(max_length=500, required=True)
