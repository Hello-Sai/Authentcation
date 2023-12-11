# Authentcation


# OTP Authentication

First of all You need to setup twillio account_sid and auth_token in settings.py

file![image](https://github.com/Hello-Sai/Authentcation/assets/90458132/eec5b376-92c5-4c1e-b7db-6577b7db5382)


These are my Urls 

![image](https://github.com/Hello-Sai/Authentcation/assets/90458132/7819411a-d9b7-4fd4-875b-b75d0f0f531c)

I used Post man for my testing

http://localhost:8000/accounts/register   specify json data as { "phone_number" : xxxxx}

# POST Method

![image](https://github.com/Hello-Sai/Authentcation/assets/90458132/7f5196cd-41df-4503-b48e-6411dc26616e)

After entering You will get the otp message on your mobile 

![Untitled](https://github.com/Hello-Sai/Authentcation/assets/90458132/50a1202c-be3f-4d43-9038-59dbcf4300f6)

# http://127.0.0.1:8000/accounts/otp POST specify Json Data as {"otp":xxxx}

![image](https://github.com/Hello-Sai/Authentcation/assets/90458132/60b6d150-75d2-47b2-bd11-c43be15b7a9f)

After Entered go to home

# i.e : http://127.0.0.1:8000/accounts/home GET 

![Untitled](https://github.com/Hello-Sai/Authentcation/assets/90458132/9952a794-fe0f-4b86-a09b-e7cd66ab83f0)

as of now I displayed only phonenumber

and same as for login also 

for logout
# http://127.0.0.1:8000/accounts/logout GET
![image](https://github.com/Hello-Sai/Authentcation/assets/90458132/38791916-91a1-4b11-ae15-18035689f4d1)

This is my OTP authentication module
