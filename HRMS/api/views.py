from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serializer import *
from .models import *


# class CustomerSignup(APIView):
#     def post(self,request):
#         serializer = CustomerSignupSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.data["username"]
#             password = serializer.data['password']
#             mobile = serializer.data["mobile"]

#         customerDetails = list(customerData.objects.filter(mobile=mobile).values())
#         if len(customerDetails) == 0:
#             customerData.objects.create(username=username,password=password,mobile=mobile)
#             message = {"Message":"signup successfully"}
#             return JsonResponse(message,status=status.HTTP_201_CREATED,safe=False)
#         else:
#             message = {"Message": "Username already exist"}
#             return JsonResponse(message,status=status.HTTP_400_BAD_REQUEST,safe=False)
        
class CustomerSignup(APIView):
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.data["username"]
                mobile = serializer.data["mobile"]
                password = serializer.data["password"]
                fname = serializer.data["fname"]
                lname = serializer.data["lname"]
                address = serializer.data["address"]
                age = serializer.data["age"]
                Customer.objects.filter(username=username).create(
                    username=username,
                    mobile=mobile,
                    password=password,
                    fname=fname,
                    lname=lname,
                    address=address,
                    age=age)
                message = {"message":"Signed Up successfully"}
                return JsonResponse(message,status=status.HTTP_202_ACCEPTED,safe=False)
            except Exception as e:
                message = {"Error": str(e)}
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST, safe=False)

        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Customerlogin(APIView):
    def post(self,request):
        serializer = CustomerloginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data["username"]
            password = serializer.data["password"]

            customerDetails = list(Customer.objects.filter(username=username).values())
            if len(customerDetails) == 1:
                Customer.objects.filter(username=username,password=password)
                message = {"Message":"Login successfull"}
                return JsonResponse(message,status=status.HTTP_201_CREATED)
            else:
                message = {"Message":"Invalid credentials"}
                return JsonResponse(message,status=status.HTTP_400_BAD_REQUEST)
