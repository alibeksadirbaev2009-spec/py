import sqlite3

class User:
    def __init__(self, id: int, name: str, lastname: str, birth: str, location: str, phone: str, email:str):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.birth = birth
        self.location = location 
        self.phone = phone
        self.email = email


class UserService:
    def __init__(self, filename: str = "database.sql"):
        self.db = sqlite3.connect(filename)
        self.cur = self.db.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users_info (
            id INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            lastname VARCHAR,
            birth VARCHAR,
            location VARCHAR,
            phone VARCHAR,
            email VARCHAR NOT NULL
        );
        """)
        
    def create(self, name: str, lastname: str, birth: str, location: str, phone: str, email: str):
        self.cur.execute("""
        INSERT INTO users_info (name, lastname, birth, location, phone, email) VALUES (?, ?, ?, ?, ?, ?);
        """, ('Jhon', 'Smiths', '1998', 'California', '+1 (565) 234-5445', 'jhon@gmail.com'))

        self.cur.execute("""
        INSERT INTO users_info (name, lastname, birth, location, phone, email) VALUES (?, ?, ?, ?, ?, ?);
        """, ('Anna', 'Yuki', '2005', 'Texas', '+1 (434) 453-4223', 'yuki@gmail.com'))

        self.cur.execute("""
        INSERT INTO users_info (name, lastname, birth, location, phone, email) VALUES (?, ?, ?, ?, ?, ?);
        """, ('Tomas', 'White', '2000', 'Los-Angeles', '+1 (456) 995-2233', 'tomas@gmail.com'))
        
        self.db.commit()
    
    def get(self) -> list[User]:
        self.cur.execute("SELECT * FROM users_info;")
        data = self.cur.fetchall()
        result = []
        for i in data:
            result.append(User(
                id=i[0],
                name=i[1],
                lastname=i[2],
                birth=i[3],
                location=i[4],
                phone=i[5],
                email=i[6]
            ))
        return result
    
    def get_by_id(self, _id: int) -> User:
        self.cur.execute(f"SELECT * FROM users_info WHERE id = {_id};")
        data = self.cur.fetchone()
        return User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    
    def update(self, _id: int, name: str | None = None, lastname: str | None = None,
                birth: str | None = None, location: str | None = None, phone: str | None = None,
                email: str | None = None):
        if name is None and lastname is None and birth is None and location is None and phone is None and email is None:
            raise Exception("Both parameters must not be empty!")
        stmt = f"UPDATE users_info SET "
        params = []
        if name is not None:
            params.append("name = " + name)
        
        if lastname is not None:
            params.append("lastname = " + lastname)
        
        if birth is not None:
            params.append("birth = " + birth)

        if location is not None:
            params.append("location = " + location)

        if phone is not None:
            params.append("phone = " + phone)

        if email is not None:
            params.append("email = " + email)
        

        stmt = stmt + ", ".join(params) + f" WHERE id = {_id};"
        self.cur.execute(stmt)
        self.db.commit()
    
    def delete(self, id: int):
        self.cur.execute(f"DELETE FROM users_info WHERE id = 4")
        self.db.commit()
    def close(self):
        self.db.close()


    def get_age(self):
        from datetime import datetime
        return datetime.now().year - int(self.birth)#
     

    def close(self):
        self.db.close()
print(UserService.get_age())

# service = UserService()

# service.create("Jhon", "Smiths", "1998", "California", "+1 (565) 234-5445", "jhon@gmail.com")
# service.create("Anna", "Yuki", "2005", "Texas", "+1 (434) 453-4223", "yuki@gmail.com")
# service.create("Tomas", "White", "2000", "Los-Angeles", "+1 (456) 995-2233", "tomas@gmail.com")
# users = service.get()
# for k in users:
#         print(k)

# ROW, COLUMB