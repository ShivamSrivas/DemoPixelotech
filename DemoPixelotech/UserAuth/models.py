
from django.db import models

class UserProfile(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=15)
    Password = models.CharField(max_length=128)  # You might want to use Django's built-in password hashing mechanisms instead of storing plaintext passwords

    def __str__(self):
        return self.name
