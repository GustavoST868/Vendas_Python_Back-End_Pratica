import sqlite3

class Address:
    def __init__(self):
        self.connection = sqlite3.connect('addresses.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT NOT NULL,
                state TEXT NOT NULL,
                city TEXT NOT NULL,
                street TEXT NOT NULL,
                number INTEGER NOT NULL,
                complement TEXT
            )
        ''')
        self.connection.commit()

    def insert_address(self, country, state, city, street, number, complement):
        self.cursor.execute('''
            INSERT INTO addresses (country, state, city, street, number, complement)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (country, state, city, street, number, complement))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()