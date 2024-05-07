from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from UserAuth.models import UserProfile
from random import randint
from UserAuth.services import UserAuth
import json

user_auth = UserAuth(ProcessId=randint(0000,1111))

csrf_exempt
def Verification(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            phone_number = json_data.get('phone_number')
            email_recipient = json_data.get('email_recipient')
            if phone_number or email_recipient:
                otp = user_auth.PhoneNumberVerification(phone_number,email_recipient)
                if otp:
                    return JsonResponse({'otp': otp, 'message': 'OTP sent successfully'})
                else:
                    return JsonResponse({'message': 'Failed to send OTP'}, status=500)
            else:
                return JsonResponse({'message': 'Phone or Email is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
    

@csrf_exempt
def UserRegistration(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        name = json_data.get('name')
        email = json_data.get('email')
        phone_number = json_data.get('phone_number')
        password = json_data.get('password')
        
        if name and email and phone_number and password:
            user = user_auth.UserRegistration(name, email, phone_number, password)
            if isinstance(user, UserProfile):
                return JsonResponse({'message': 'User registered successfully'})
            else:
                return JsonResponse({'message': str(user)}, status=500)
        else:
            return JsonResponse({'message': 'All fields are required'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
