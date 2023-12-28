import sqlite3

class User:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                administrador INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_user(self, name, password, administrador):
        self.cursor.execute('''
            INSERT INTO users (name, password, administrador)
            VALUES (?, ?, ?)
        ''', (name, password, administrador))
        self.connection.commit()

    def user_exists(self, name, password):
        self.cursor.execute('SELECT * FROM users WHERE name = ? AND password = ?', (name, password))
        return self.cursor.fetchone() is not None

    def close_connection(self):
        self.connection.close()