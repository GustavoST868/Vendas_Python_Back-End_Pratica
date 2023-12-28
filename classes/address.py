import sqlite3

class Address:
    def __init__(self, country, state, city, street, number, cep, complement):
        self.country = country
        self.state = state
        self.city = city
        self.street = street
        self.number = number
        self.cep = cep
        self.complement = complement
        self.create_address_table()
        self.insert_address()

    def create_address_table(self):
        with sqlite3.connect("addresses.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS addresses (
                country TEXT,
                state TEXT,
                city TEXT,
                street TEXT,
                number TEXT,
                cep TEXT,
                complement TEXT
            )
            ''')

    def insert_address(self):
        with sqlite3.connect("addresses.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO addresses VALUES (?,?,?,?,?,?,?)",
                           (self.country, self.state, self.city, self.street, self.number, self.cep, self.complement))

    @staticmethod
    def get_address(country, state, city, street, number):
        with sqlite3.connect("addresses.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM addresses WHERE country=? AND state=? AND city=? AND street=? AND number=?",
                           (country, state, city, street, number))
            address_data = cursor.fetchone()
            if address_data:
                return Address(*address_data)
            return None

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
