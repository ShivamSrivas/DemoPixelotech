from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from UserAuth.models import UserProfile
from UserAuth.services import UserAuth

# Instantiate UserAuth class
user_auth = UserAuth(ProcessId="12")

@csrf_exempt
def PhoneNumberVerification(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if phone_number:
            otp = user_auth.PhoneNumberVerification(phone_number)
            if otp:
                return JsonResponse({'otp': otp,'message':'otp sent successfully'})
            else:
                return JsonResponse({'message': 'Failed to send OTP'}, status=500)
        else:
            return JsonResponse({'message': 'Phone number is required'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def UserRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
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
