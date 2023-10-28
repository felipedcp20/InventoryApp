from typing import List
from mysql.connector import connect
from app.controller.users import User

def get_users(conn: connect) -> List[User]:
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    users = [User(**row) for row in result]
    cursor.close()
    return users
