import sqlite3

class DatabaseAdministrators:
    def __init__(self, data):
        # Constructor to initialize the instance with provided data
        self.data = data
        self.assign_data()
        self.connect_database()
        self.create_table()

    # Method for assigning data attributes
    def assign_data(self):
        administrator_data = self.split_data()
        self.name = administrator_data['name']
        self.password = administrator_data['password']
        self.email = administrator_data['email']
        self.birth_date = administrator_data['birth_date']
        self.gender = administrator_data['gender']
        self.phone = administrator_data['phone']

    # Method for connecting to the SQLite database
    def connect_database(self):
        self.conn = sqlite3.connect('administrators.db')
        self.cursor = self.conn.cursor()

    # Method for creating the administrators table in the database
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                password TEXT,
                email TEXT,
                birth_date TEXT,
                gender TEXT,
                phone TEXT
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
            INSERT INTO administrators (name, password, email, birth_date, gender, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.password, self.email, self.birth_date, self.gender, self.phone))
        self.conn.commit()

    # Method for fetching data from the administrators table
    def get_data(self, administrator_name):
        self.cursor.execute('SELECT * FROM administrators WHERE name = ?', (administrator_name,))
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
    def delete_data(self, administrator_name):
        self.cursor.execute('DELETE FROM administrators WHERE name = ?', (administrator_name,))
        self.conn.commit()

    # Method for checking if an administrator exists in the database
    def administrator_exists(self, administrator_name):
        result = self.get_data(administrator_name)
        return result is not None
