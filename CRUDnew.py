
from MyDataBase import MyDatabase
from Constants import Constants

class CRUD:
    const = Constants()
    conn = MyDatabase(
            const.decrypt(Constants.e_host),
            int(const.decrypt(Constants.e_port)),
            const.decrypt(Constants.e_database),
            const.decrypt(Constants.e_user),
            const.decrypt(Constants.e_password)
        )
    
    def create_profile(self):
        sql  = '''
        CREATE TABLE IF NOT EXISTS defaultdb.profiles (
            idx INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            alias VARCHAR(255) NOT NULL,
            token VARCHAR(255) NOT NULL,
            birthdate DATE NOT NULL,
            email VARCHAR(255) NOT NULL,
            lang_code VARCHAR(10) NOT NULL,
            routine BOOLEAN NOT NULL,
            alarm BOOLEAN NOT NULL,
            inactivity_time INTEGER NOT NULL,
            inactivity_type VARCHAR(50) NOT NULL
        );  
'''
        result = self.conn.query(sql)
        print(result)

    def get_profile(self):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.profiles;"
        result = self.conn.query(sql) 
        print(result)

    def set_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type):
        sql = "INSERT INTO defaultdb.profiles " \
        "(name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type) " \
        "VALUES('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}');".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type
            )
        result = self.conn.query(sql) 
        print(result)

    def update_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx):
        sql = "UPDATE defaultdb.profiles " \
        "SET name='{}', alias='{}', token='{}', birthdate={}, email='{}', lang_code='{}', `routine`={}, alarm={}, inactivity_time={}, inactivity_type={} " \
        "WHERE idx={};".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx
            )

    def delete_profile(self, idx):
        sql = "DELETE FROM defaultdb.profiles " \
        "WHERE idx={};".format(idx)

crud = CRUD()
#crud.create_profile()
crud.set_profile("John Doe", "johndoe", "token123", "1990-01-01", "john.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("jonatha segura", "jony", "token163", "2006-12-07", "jony.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("eishel alexandra", "ale", "token923", "2009-12-23", "ale.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("Camila", "camilita", "token123", "1490-11-21", "camila.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("gerardo gutierrez", "gera", "token193", "1890-11-31", "gera.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("fernando lopez", "fernando", "token125", "2011-02-22", "lopez.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("Zianya cervantes", "zian", "token023", "2005-01-05", "zian.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("Nicole avelar", "nico", "token193", "1980-01-01", "nico.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("daphne paprica", "daph", "token933", "1390-01-11", "daph.doe@example.com", "en", True, True, 300, "aaaa")   
crud.set_profile("Emilio zalasar", "emi", "token663", "1999-01-21", "emi.doe@example.com", "en", True, True, 300, "aaaa")   