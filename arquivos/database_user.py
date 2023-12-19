import sqlite3

class DatabaseUser:
    def __init__(self, user_data):
        self.data = user_data
        self.assign_data()

    def assign_data(self):
        user_data = self.split_data()
        self.name = user_data['name']
        self.password = user_data['password']
        self.email = user_data['email']
        self.birth_date = user_data['birth_date']
        self.gender = user_data['gender']
        self.phone = user_data['phone']
        self.connect_database()
        self.create_table()

    def connect_database(self):
        try:
            self.conn = sqlite3.connect('user.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

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

    def split_data(self):
        separated_data = {}
        lines = self.data.strip().split('\n')

        for line in lines:
            key, value = line.strip().split(':')
            separated_data[key] = value

        return separated_data

    def insert_data(self):
        try:
            self.cursor.execute('''
                INSERT INTO user (name, password, email, birth_date, gender, phone)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.name, self.password, self.email, self.birth_date, self.gender, self.phone))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

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

    def delete_data(self, user_name):
        self.cursor.execute('DELETE FROM user WHERE name = ?', (user_name,))
        self.conn.commit()

    def user_exists(self, user_name):
        result = self.get_data(user_name)
        return result is not None
