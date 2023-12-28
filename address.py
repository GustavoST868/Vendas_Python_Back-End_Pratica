class Address:
    def __init__(self, country, state, city, street, number, cep, complement):
        self.country = country
        self.state = state
        self.city = city
        self.street = street
        self.number = number
        self.cep = cep
        self.complement = complement

    def getCountry(self):
        return self.country
    
    def getState(self):
        return self.state
    
    def getCity(self):
        return self.city
    
    def getStreet(self):
        return self.street
    
    def getNumber(self):
        return self.number

    def getCep(self):
        return self.cep
    
    def getComplement(self):
        return self.complement

    def setCountry(self, country):
        self.country = country
    
    def setState(self, state):
        self.state = state
    
    def setCity(self, city):
        self.city = city
    
    def setStreet(self, street):
        self.street = street
    
    def setNumber(self, number):
        self.number = number

    def setCep(self, cep):
        self.cep = cep
    
    def setComplement(self, complement):
        self.complement = complement

    def ToString(self):
        string = {
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'street': self.street,
            'number': self.number,
            'cep': self.cep,
            'complement': self.complement
        }
        return string
