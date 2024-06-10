import sqlite3
 

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query,params)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()



# class Dog:
#     def __init__(self, breed, age, owner):
#         self.breed = breed
#         self.age = age