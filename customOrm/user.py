from model import BaseModel

class User(BaseModel):
    table_name = "users"

    fields = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "username":"TEXT",
        "bio":"TEXT"
    }

User.create_table()

newUser = User(username="john Doe", bio="Ativist")
print(newUser.addItem())