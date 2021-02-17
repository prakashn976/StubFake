 
  
class Fake:
    usernames_password={}

    usernames_password["Prakash"]="Prakash123"
    usernames_password["Prakashsh"]="1234"
    
    def validate_cerdentials(self,username,password):
        if Fake.usernames_password[username]==password:
            return True
        else:
            return False
    