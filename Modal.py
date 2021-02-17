from Stub import Fake 

class Login:
    
    def check_login(self,username,password):
        result=Fake.validate_cerdentials(self,username,password)
        if result==True:
            return "Login Successful"
        else:
            return "Login Failed"