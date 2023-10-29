from base_database import Database


class MatrizDb:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def create_matriz(self, cod_system, name_profile, cod_system_conflict, name_profile_conflict ):
        self.cursor.execute('INSERT INTO matriz VALUES (?,?,?,?)', (cod_system, name_profile, cod_system_conflict, name_profile_conflict))
        self.db.save_db()

    def see_matriz(self):
        self.cursor.execute('SELECT * FROM matriz')
        result = self.cursor.fetchall()
        return result
