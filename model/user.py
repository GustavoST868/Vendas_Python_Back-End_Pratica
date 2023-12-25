class User:
    def __init__(self, name, password, email, is_administrator):
        self.name = name
        self.password = password
        self.email = email
        self.is_administrator = is_administrator

    def user_return(self):
        return {
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'is_administrator': self.is_administrator
        }

    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email

    def is_administrator(self):
        return self.is_administrator
