import sqlite3

class DatabaseProduct:
    def __init__(self, data):
        # Constructor to initialize the instance with provided data
        self.data = data
        self.assign_data()
        self.connect_database()
        self.create_table()

    # Method for assigning data attributes
    def assign_data(self):
        product_data = self.split_data()
        self.id = product_data['id']
        self.name = product_data['name']
        self.description = product_data['description']
        self.price = product_data['price']
        self.size = product_data['size']
       

    # Method for connecting to the SQLite database
    def connect_database(self):
        self.conn = sqlite3.connect('product.db')
        self.cursor = self.conn.cursor()

    # Method for creating the administrators table in the database
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price TEXT,
                size TEXT,
            )
        ''')
        self.conn.commit()

    # Method for separating data into key-value pairs
    def split_data(self):
        separated_data = {}
        lines = self.data.strip().split('\n')
        
        for line in lines:
            key, value = line.strip().split(':')
            separated_data[key] = value
        
        return separated_data

    # Method for inserting data into the administrators table
    def insert_data(self):
        self.cursor.execute('''
            INSERT INTO administrators (name, description, price, size)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.description, self.price, self.size))
        self.conn.commit()

    # Method for fetching data from the administrators table
    def get_data(self, product_name):
        self.cursor.execute('SELECT * FROM administrators WHERE name = ?', (product_name,))
        data = self.cursor.fetchone()

        if data:
            table_format = f'''
            +----+------------+--------------+--------------------+------------+--------+-------------+
            | ID |    Name    |   Password   |       Email        | Birth Date | Gender |    Phone    |
            +----+------------+--------------+--------------------+------------+--------+-------------+
            | {data[0]:<2} | {data[1]:<10} | {data[2]:<13} | {data[3]:<18} | {data[4]:<10} | {data[5]:<6} | {data[6]:<11} |
            +----+------------+--------------+--------------------+------------+--------+-------------+
            '''
            return table_format
        else:
            return "Administrator not found."
        
    # Method for deleting data from the administrators table
    def delete_data(self, product_name):
        self.cursor.execute('DELETE FROM administrators WHERE name = ?', (product_name,))
        self.conn.commit()

    # Method for checking if an administrator exists in the database
    def administrator_exists(self, product_name):
        result = self.get_data(product_name)
        return result is not None