import sqlite3

class User:
    def __init__(self, name="", password="", email="", is_administrator=False):
        self.name = name
        self.password = password
        self.email = email
        self.is_administrator = is_administrator
        self.create_user_table()
        self.insert_user()

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        self.insert_user()

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        # Implement secure password hashing here
        self.password = password
        self.insert_user()

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
        self.insert_user()

    def is_admin(self):
        return self.is_administrator
    
    def set_admin(self, is_administrator):
        self.is_administrator = is_administrator
        self.insert_user()

    def to_string(self):
        user_data = {
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'is_administrator': self.is_administrator
        }
        return user_data
    
    def create_user_table(self):
        with sqlite3.connect("users.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT PRIMARY KEY,
                password TEXT,
                email TEXT,
                is_admin BOOLEAN
            )
            ''')

    def insert_user(self):
        with sqlite3.connect("users.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?,?)",
                           (self.name, self.password, self.email, bool(self.is_administrator)))

    @staticmethod
    def get_user(username):
        with sqlite3.connect("users.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name=?", (username,))
            user_data = cursor.fetchone()
            if user_data:
                return User(*user_data)
            return None 

    @staticmethod
    def user_exists(username):
        with sqlite3.connect("users.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE name=?)", (username,))
            return cursor.fetchone()[0] == 1
