class Address:
    def __init__(self,number,neighborhood,city,state,country,complement):
        self.number = number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.complement = complement

    def get_address(self):
        address = f'''
        number:{self.number}
        neighbordhood:{self.neighborhood}
        city:{self.city}
        state:{self.state}
        country:{self.country}
        complement:{self.complement}
                   '''
        return address