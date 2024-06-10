from model import BaseModel;

class Dog(BaseModel):
    table_name = "dog"

    fields={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "breed": "Text"

    }

Dog.create_table()

newDog = Dog()
