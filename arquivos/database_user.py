# database_user.py
import sqlite3

class DatabaseUser:
     # Constructor to initialize the instance with provided data
    def __init__(self, data):
        self.data = data
        self.assign_data()
        self.connect_database()
        self.create_table()

     # Method for assigning data attributes
    def assign_data(self):
        user_data = self.split_data()
        self.name = user_data['name']
        self.password = user_data['password']
        self.email = user_data['email']
        self.birth_date = user_data['birth_date']
        self.gender = user_data['gender']
        self.phone = user_data['phone']

     #Method for connecting to the SQLite database
    def connect_database(self):
        with sqlite3.connect('user.db') as conn:
            self.conn = conn
            self.cursor = conn.cursor()

    # Method for creating the user table in the database
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
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

    # Method for inserting data into the user table
    def insert_data(self):
        self.cursor.execute('''
            INSERT INTO user (name, password, email, birth_date, gender, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.password, self.email, self.birth_date, self.gender, self.phone))
        self.conn.commit()

    # Method for fetching data from the user table
    def get_data(self, user_name):
        self.cursor.execute('SELECT * FROM user WHERE name = ?', (user_name,))
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
            return "User not found."

    # Method for deleting data from the user table
    def delete_data(self, user_name):
        self.cursor.execute('DELETE FROM user WHERE name = ?', (user_name,))
        self.conn.commit()

    # Method for checking if an user exists in the database
    def user_exists(self, user_name):
        result = self.get_data(user_name)
        return result is not None
