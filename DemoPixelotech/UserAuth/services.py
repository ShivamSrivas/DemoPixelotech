import requests
import random
from Log.logger import logger_call
from .models import UserProfile
from DemoPixelotech.settings import API_KEY , EMAIL_KEY
import smtplib
from DemoPixelotech.settings import EMAIL


class UserAuth():
    def __init__(self,ProcessId):
        self.ProcessId = ProcessId

    def PhoneNumberVerification(self, PhoneNumber=None, EmailRecipient=None):
        """
        Sends a one-time password (OTP) for phone number or email verification.

        Args:
            PhoneNumber (str): The phone number to which OTP needs to be sent.
            EmailRecipient (str): The email address to which OTP needs to be sent.

        Returns:
            int or str: The OTP if successfully sent, else returns an error message.

        Raises:
            ValueError: If neither PhoneNumber nor EmailRecipient is provided.
            Exception: If any other unexpected error occurs.
        """

        # Generate a random OTP
        otp = random.randint(1000, 2222)

        try:
            if PhoneNumber:
                # Send OTP via SMS/Call
                try:
                    url = f"https://2factor.in/API/V1/{API_KEY}/SMS/{PhoneNumber}/{otp}"
                    response = requests.get(url)
                    response.raise_for_status()  # Raise an exception for non-200 status codes
                    logger_call("/Log/UserAuth.log", self.ProcessId, "OTP sent via SMS", "Info")
                    return otp
                except requests.RequestException as sms_error:
                    logger_call("/Log/UserAuth.log", self.ProcessId, f"Error sending OTP via SMS: {sms_error}", "Error")
                    return str(sms_error)

            elif EmailRecipient:
                # Send OTP via Email
                try:
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(EMAIL["sender_email"], EMAIL_KEY)
                    server.sendmail(EMAIL["sender_email"], EmailRecipient, msg=str(otp))
                    server.quit()
                    logger_call("/Log/UserAuth.log", self.ProcessId, "OTP sent via email", "Info")
                    return otp
                except smtplib.SMTPAuthenticationError as auth_error:
                    logger_call("/Log/UserAuth.log", self.ProcessId, f"SMTP authentication error: {auth_error}", "Error")
                    return str(auth_error)
                except smtplib.SMTPException as email_error:
                    logger_call("/Log/UserAuth.log", self.ProcessId, f"Error sending OTP via email: {email_error}", "Error")
                    return str(email_error)

            else:
                raise ValueError("Neither PhoneNumber nor EmailRecipient provided.")

        except Exception as error:
            logger_call("/Log/UserAuth.log", self.ProcessId, f"Unexpected error: {error}", "Error")
            return str(error)
    
    def UserRegistration(self, Name, Email, PhoneNumber, Password):
        try:
            logger_call("/Log/UserAuth.log", self.ProcessId, f"A new user is created with {Name},having email as {Email} with {PhoneNumber} phone no.", "Info")
            user = UserProfile(Name=Name, Email=Email, PhoneNumber=PhoneNumber, Password=Password)
            user.save()
            return user
        except Exception as error:
            return error
