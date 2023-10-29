from base_database import Database


class SystemsDb:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def create_system(self, cod_system, name_system):
        self.cursor.execute('INSERT INTO systems VALUES (?,?)', (cod_system, name_system))
        self.db.save_db()

    def delete_system(self, cod_system):
        self.cursor.execute('DELETE FROM systems WHERE cod_system = ?', (cod_system,))
        self.db.save_db()

    def see_systems(self):
        self.cursor.execute('SELECT * FROM systems')
        result = self.cursor.fetchall()
        return result

    def search_id(self, id_sistema):
        self.cursor.execute('SELECT id FROM systems WHERE id = ?', (id_sistema,))
        result = self.cursor.fetchall()
        return result