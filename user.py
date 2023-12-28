class User:
    def __init__(self, name, password, email, is_administrator):
        self.name = name
        self.password = password
        self.email = email
        self.is_administrator = is_administrator

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def is_admin(self):
        return self.is_administrator
    
    def set_admin(self, is_administrator):
        self.is_administrator = is_administrator

    def to_string(self):
        user_data = {
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'is_administrator': self.is_administrator
        }
        return user_data
