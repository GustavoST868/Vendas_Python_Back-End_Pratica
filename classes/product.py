import sqlite3
class Product:
    def __init__(self,name,size,description,price):
        self.name = name
        self.size = size
        self.description = description
        self.price = price
        self.create_product_table()
        self.insert_product()

    def getName(self):
        return self.name
    
    def getSizer(self):
        return self.size
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def setName(self,name):
        self.name = name
    
    def setSizer(self,size):
       self.size = size
    
    def setDescription(self,description):
        self.description = description
    
    def setPrice(self,price):
        self.price = price

    
    
    def create_product_table(self):
        with sqlite3.connect("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                name TEXT,
                size TEXT,
                description TEXT,
                price REAL
            )
            ''')

    def insert_product(self):
        with sqlite3.connect("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products VALUES (?,?,?,?)",
                           (self.name, self.size, self.description, self.price))

    @staticmethod
    def is_product_in_database(product_name):
        with sqlite3.connect("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
            return cursor.fetchone() is not None

    def to_string(self):
        string = {
            'name': self.name,
            'size': self.size,
            'description': self.description,
            'price': self.price
        }
        return string
    