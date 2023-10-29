from base_database import Database


class ProfileDb:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def create_profile(self, cod_system, name_profile, description):
        self.cursor.execute('INSERT INTO profiles VALUES (?,?,?)', (cod_system, name_profile, description))
        self.db.save_db()

    def delete_profile(self, name_profile):
        self.cursor.execute('DELETE FROM profiles WHERE name_profile = ?', (name_profile,))
        self.db.save_db()

    def see_profiles(self):
        self.cursor.execute('SELECT * FROM profiles')
        result = self.cursor.fetchall()
        return result


