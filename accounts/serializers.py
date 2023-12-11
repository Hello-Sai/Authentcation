
from accounts.utils import send_otp
from .models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
class UserSerializer(ModelSerializer):
    phone_number = serializers.CharField(required=True,max_length=10)
    class Meta:
        model = User
        fields = ('phone_number',)

    def validate(self, data):
        self.mobile =  data.get('phone_number')
        symbols = "+-`~!#@$%^&*()-=,<>./?\"';:[]"
        
        if any(symbol in self.mobile for symbol in symbols):
            raise ValidationError("Error Please do not use special characters")
        if not len(self.mobile)==10:
            raise ValidationError("Enter valid 10 digit mobile number")
        if not self.mobile.isdigit():
            raise ValidationError("please enter valid numbers only")
        return data    
    
    def register(self):
        phone_number = self.validated_data['phone_number']
        try:
            otp = send_otp(phone_number)
        except Exception as e:
            serializers.ValidationError("%s"%e)
        self.save()
        self.instance.otp= otp
        self.instance.save()

    def login(self):
        phone_number = self.data['phone_number']

        try:
            profile =User.objects.get(phone_number=phone_number)
            print(profile)
            try:
                otp = send_otp(phone_number)
            except Exception as e:
                raise ValidationError("You are Not Connected to internet got following error -> %s"%e)
        except Exception as e:
            print('except executed %s'%e)
            raise ValidationError("You are Not Exists")
        profile.otp = otp
        profile.save()
        
