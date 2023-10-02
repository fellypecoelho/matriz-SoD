import sqlite3
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def save_db(self):
        self.conn.commit()

    def close_db(self):
        self.conn.close()

