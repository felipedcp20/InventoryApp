from typing import List
import mysql.connector
from app.models.user import User

def get_users(conn: mysql.connector.MySQLConnection) -> List[User]:
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    users = []
    for record in result:
        user = User(
            id=record[0],
            username=record[1],
            email=record[2],
            password=record[3],
            full_name=record[4],
            is_active=bool(record[5]),
            is_superuser=bool(record[6]),
            role=record[7]
        )
        users.append(user)
        
    cursor.close()
    return users
