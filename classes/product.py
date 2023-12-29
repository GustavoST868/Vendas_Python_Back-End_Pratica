import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                size TEXT,
                description TEXT
            )
        ''')
        self.conn.commit()
        self.insert_product()

    def insert_product(self, name, price, size, description):
        self.cursor.execute('''
            INSERT INTO products (name, price, size, description)
            VALUES (?, ?, ?, ?)
        ''', (name, price, size, description))
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def check_product_exists(self, name):
        self.cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
        return self.cursor.fetchone() is not None