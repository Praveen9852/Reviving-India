from rest_framework import serializers


    
class CustomerSignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100,required=False)
    mobile = serializers.IntegerField(required=False)
    password = serializers.CharField(max_length=50)
    fname = serializers.CharField(max_length=50,required=False)
    lname = serializers.CharField(max_length=50,required=False)
    address = serializers.CharField(max_length=200,required=False)
    age = serializers.IntegerField(required=False)


class CustomerloginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
