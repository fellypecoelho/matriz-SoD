from base_database import Database

class User_db:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def create_user(self, cpf, cod_system, profile):
        self.cursor.execute('INSERT INTO users VALUES (?,?,?)', (cpf, cod_system, profile))
        self.db.save_db()

    def delete_user(self, cpf):
        self.cursor.execute('DELETE FROM users WHERE cpf = ?', (cpf,))
        self.db.save_db()

    def see_users(self):
        self.cursor.execute('SELECT * FROM users')
        result = self.cursor.fetchall()
        return result

