#"is_user" is boolean indicator that the user is an administrator
class User:
    def __init__(self,name,passworld,email,is_administrator):
        self.name = name
        self.passworld = passworld
        self.email = email
        self.is_administrator = is_administrator

    def user_return(self):
        user_data = {
            'name': self.name,
            'password': self.passworld,
            'email': self.email,
            'is_administrator': self.is_administrator
        }
        return user_data
    

t = User("Gustavo","lngg1234","gusta@gmail.com",True)
print(t.user_return())