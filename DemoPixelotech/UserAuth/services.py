import requests
import random
from Log.logger import logger_call


class UserRegisteration():
    def __init__(self,ProcessId):
        self.ProcessId = ProcessId

    def UserRegistrationByPhone(self,PhoneNumber):
        try:
            logger_call("Log/UserAuth.log",self.ProcessId,"UserRegistrationByPhone Is Invoked","Info")
            otp = random.randint(1000,2222)
            api_key="833244f2-0bde-11ef-8cbb-0200cd936042"
            url=f"https://2factor.in/API/V1/{api_key}/SMS/{PhoneNumber}/{otp}"
            data=requests.get(url)
            if data.status_code:
                logger_call("Log/UserAuth.log",self.ProcessId,"Otp is sent","Info")
                return otp
        except Exception as e:
            logger_call("Log/UserAuth.log",self.ProcessId,"There's an error in UserRegistrationByPhone method saying --> " + str(e),"Error")
            return e
        
   

        

obj = UserRegisteration(1234)
print(obj.UserRegistrationByPhone(8853157886))
