import requests

class UserRegisteration():
    def UserRegistrationByPhone(self,PhoneNumber):
        try:
            url=""
            data=requests.get(url)
            return data
        except Exception as e:
            return e
