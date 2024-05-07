import requests
import random
from Log.logger import logger_call
from .models import UserProfile

class UserAuth():
    def __init__(self,ProcessId):
        self.ProcessId = ProcessId

    def PhoneNumberVerification(self,PhoneNumber):
        try:
            logger_call("D:/DemoPixelotech/Log/UserAuth",self.ProcessId,"UserRegistrationByPhone Is Invoked","Info")
            otp = random.randint(1000,2222)
            api_key="833244f2-0bde-11ef-8cbb-0200cd936042"
            url=f"https://2factor.in/API/V1/{api_key}/SMS/{PhoneNumber}/{otp}"
            data=requests.get(url)
            if data.status_code:
                logger_call("Log/UserAuth.log",self.ProcessId,"Otp is sent","Info")
                return otp
        except Exception as error:
            logger_call("Log/UserAuth.log",self.ProcessId,"There's an error in UserRegistrationByPhone method saying --> " + str(error),"Error")
            return error
    
    def UserRegistration(self, Name, Email, PhoneNumber, Password):
        try:
            user = UserProfile(Name=Name, Email=Email, PhoneNumber=PhoneNumber, Password=Password)
            user.save()
            return user
        except Exception as error:
            return error
    
        
obj = UserAuth(1234)
obj.PhoneNumberVerification(8853157886)
# obj.UserRegistration("Shivam Srivastava","shivamsri@gmail.com","9305055096","123@")
