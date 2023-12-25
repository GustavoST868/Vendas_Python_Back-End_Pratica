class User:
    def __init__(self, name, password, email, is_administrator):
        self.name = name
        self.password = password
        self.email = email
        self.is_administrator = is_administrator

    def user_return(self):
        user_data = {
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'is_administrator': self.is_administrator
        }
        return user_data

    def unpack_user_data(self, user_data):
        name = user_data['name']
        password = user_data['password']
        email = user_data['email']
        is_administrator = user_data['is_administrator']
        return name, password, email, is_administrator


t = User("Gustavo", "lngg1234", "gusta@gmail.com", True)
user_data = t.user_return()
name, password, email, is_administrator = t.unpack_user_data(user_data)


