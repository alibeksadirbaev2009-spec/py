from fastapi import FastAPI, HTTPException
import sqlite3
from pwdlib import PasswordHash

app = FastAPI()

@app.post("/register")
async def register(firstname: str, lastname: str, username: str, age: int, password: str, reply_password: str):
    with sqlite3.connect("user.db") as conn:
        cur = conn.cursor()

        if not password == reply_password:
            raise HTTPException(
                status_code=400,
                detail="Password do not match"
            )

        check_user = cur.execute("SELECT 1 FROM users WHERE username = ? LIMIT 1", (username,))

        if check_user.fetchone():
            return {
                "message": f"Username already exists!"
            }

        hash_password = PasswordHash.recommended()
        hashed_password = hash_password.hash(password)
        cur.execute("""
        INSERT INTO users(firstname, lastname, username, age, password) 
        VALUES (?, ?, ?, ?, ?)""",
        (firstname, 
        lastname, 
        username, 
        age, 
        hashed_password
        )   
    )   
        print(hashed_password)

        conn.commit()
        return {
            "message": "OK"
        }


@app.post("/login")
async def login(username: str, password: str): 
    with sqlite3.connect("user.db") as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT password FROM users WHERE username = ?", 
            (username,)
        )

        user = cur.fetchone()

        if user is None:
            raise HTTPException(
                status_code=404, 
                detail="User not found")

        password_hash = PasswordHash.recommended()

        if not password_hash.verify(password, user[0]):
            raise HTTPException(
                status_code=401,
                detail="Invalid password"
            )

        return {
            "message": "Login successful"
        }