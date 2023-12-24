import sqlite3

class Database_Address:
    def __init__(self, data):
        self.data = data
        self.assign_data()
        self.connect_database()
        self.create_table()

    # Method for assigning data attributes
    def assign_data(self):
        administrator_data = self.split_data()
        self.number = administrator_data['number']
        self.neighborhood = administrator_data['neighborhood']
        self.city = administrator_data['city']
        self.state = administrator_data['state']
        self.country = administrator_data['country']
        self.complement = administrator_data['complement']

    # Method for connecting to the SQLite database
    def connect_database(self):
        self.conn = sqlite3.connect('address.db')
        self.cursor = self.conn.cursor()

    # Method for creating the administrators table in the database
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT,
                neighborhood TEXT,
                city TEXT,
                state TEXT,
                country TEXT,
                complement TEXT
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
            INSERT INTO administrators (number, neighborhood, city, state, country, complement)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.number, self.neighborhood, self.city, self.state, self.country, self.complement))
        self.conn.commit()

    # Method for fetching data from the administrators table
    def get_data(self, address_name):
        self.cursor.execute('SELECT * FROM administrators WHERE number = ?', (address_name,))
        data = self.cursor.fetchone()

        if data:
            table_format = f'''
            +----+--------------+--------------+--------------+--------------+--------------+--------------+
            | ID |    Number    | Neighborhood |      City    |     State    |    Country   |  Complement  |
            +----+--------------+--------------+--------------+--------------+--------------+--------------+
            | {data[0]:<2} | {data[1]:<12} | {data[2]:<12} | {data[3]:<12} | {data[4]:<12} | {data[5]:<12} | {data[6]:<12} |
            +----+--------------+--------------+--------------+--------------+--------------+--------------+
            '''
            return table_format
        else:
            return "Address not found."

    # Method for deleting data from the administrators table
    def delete_data(self, address_name):
        self.cursor.execute('DELETE FROM administrators WHERE number = ?', (address_name,))
        self.conn.commit()

    # Method for checking if an administrator exists in the database
    def administrator_exists(self, address_name):
        result = self.get_data(address_name)
        return result is not None