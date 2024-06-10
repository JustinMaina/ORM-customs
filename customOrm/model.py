from database import Database

db = Database("test.db")

class BaseModel: 
    table_name = ""
    fields = {}

    def __init__(self, **kwargs):
        for field in self.fields:
            setattr(self, field, kwargs.get(field,None))
    
    @classmethod
    def create_table(cls):
        columns = []

        for field, f_type in cls.fields.items():
            columns.append(f"{field} {f_type}")
        
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({', '.join(columns)})"

        db.execute(query)

    # add an item to a table
    # our values have to be the same number as the columns

    # INSERT INTO tablename (columns) Values (values)

    {
        "username": "TEXT",
        "BIO": "TEXT"        
    }

    ["username","bio"]
    ["?","?"]



    def addItem(self):
        fields = ", ".join(self.fields.keys())
        placeholders = ", ".join(["?"] * len(self.fields))
        values = [getattr(self, field) for field in self.fields]
        query = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
       
        db.execute(query, values)
    # query all 

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls.table_name}"
        db.execute(query)
        rows = db.fetchall()
        return rows


