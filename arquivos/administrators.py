# This class is intended to compose the set of data corresponding to administrators
class Administrator:
    def __init__(self, name, password, email, birth_date, gender, phone):
        self.name = name
        self.password = password
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.phone = phone

    # Returns the administrator data
    def get_administrator(self):
        administrator_data = f'''
        name:{self.name}
        password:{self.password}
        email:{self.email}
        birth_date:{self.birth_date}
        gender:{self.gender}
        phone:{self.phone}
        '''
        return administrator_data.strip()
