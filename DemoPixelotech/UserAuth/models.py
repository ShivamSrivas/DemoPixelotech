from django.db import models

class UserProfile(models.Model):
    """
    Model to represent user profile.
    """
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=15)
    Password = models.CharField(max_length=128) 

    def __str__(self):
        return self.Name

class EmailVerification(models.Model):
    """
    Model to store OTP for email verification.
    """
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.email}"

class PhoneVerification(models.Model):
    """
    Model to store OTP for phone number verification.
    """
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.phone_number}"
