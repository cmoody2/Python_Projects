

class User:
    def __init__(self,fName,lName,email):
        self.fName = fName
        self.lName  = lName
        self.email = email

    def active(self):
        msg = "This User is active"
        return msg

Chris = User("Chris","Moody","cmoody@rocketmail.com")

print("\n\nNew User: {} {} \nEmail: {}".format(Chris.fName,Chris.lName,Chris.email))



    

    
    
    
