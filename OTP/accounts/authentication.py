from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User
class OTPAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            otp = str(request.data["otp"])
            phone_number = request.session["phone_number"]
            user = User.objects.get(phone_number = phone_number)
            
            if otp == user.otp:
                return (user,None)
            else:
                raise AuthenticationFailed("Not a Valid OTP")
        except User.DoesNotExist:
            raise AuthenticationFailed("Not a Valid user")
        except Exception as e:
            raise Exception("Something following error Occurred -----> %s"%e)