import json
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import  UserSerializer
import random
from django.contrib import messages
# Create your views here.
from .models import User
#swagger schema

from django.contrib import auth
class HomeView(APIView):
    def get(self,request):
        phone_number = request.session.get("phone_number")
        if phone_number:
            user = User.objects.get(phone_number = phone_number)
            
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(data="User Not Logged In")
    def get_otp(self,request):
        if request.session.get("phone_number"):
            user = User.objects.get(phone_number = request.session["phone_number"])
            return Response("YOur last time entered otp is %s"%user.otp)
            
class RegisterView(APIView):
    serializer_class = UserSerializer
    def get(self,request):
        return Response("Please Register")
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        try:    
            if serializer.is_valid(raise_exception=True):
                request.session["phone_number"] = request.data["phone_number"]
                serializer.register()
                return Response("Successfully sent OTP to %s"%serializer.data.get("phone_number"))
        except Exception as e: 
            return Response(serializer.errors or "%s"%e)

class LoginView(APIView):
    serializer_class = UserSerializer
    def get(self,request):
        return Response("Please Login")
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            request.session.update({"phone_number":serializer.data["phone_number"]})
            serializer.login()
            
            return Response("Successfully sent OTP to %s"%serializer.data.get("phone_number"))
        return Response(serializer.errors)   
            

from .authentication import OTPAuthentication
class OtpView(APIView):
    authentication_classes = [OTPAuthentication]
    def post(self,request):
        try:
            auth.login(request,request.user)
            return Response("Login Successful")
        except Exception as e:
            return Response("Got some following error -> %s"%e)
        
@api_view(['GET'])
def LogoutView(request):
    if request.COOKIES.get('sessionid'):
        auth.logout(request)
        return Response("You have Successfully logged out")
    else:
        return Response("You are already logged out")

