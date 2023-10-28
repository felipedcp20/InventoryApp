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
            role=record[7],
        )
        users.append(user)

    cursor.close()
    return users


def get_user(conn: mysql.connector.MySQLConnection, user_id: int) -> User:
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    user = User(
        id=result[0][0],
        username=result[0][1],
        email=result[0][2],
        password=result[0][3],
        full_name=result[0][4],
        is_active=bool(result[0][5]),
        is_superuser=bool(result[0][6]),
        role=result[0][7],
    )
    cursor.close()
    return user


def create_user(conn: mysql.connector.MySQLConnection, user: User) -> User:
    cursor = conn.cursor()
    query = "INSERT INTO users (username, email, password, full_name, is_active, is_superuser, role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(
        query,
        (
            user.username,
            user.email,
            user.password,
            user.full_name,
            user.is_active,
            user.is_superuser,
            user.role,
        ),
    )
    conn.commit()
    cursor.close()
    return user


def update_user(
    conn: mysql.connector.MySQLConnection, user_id: int, user: User
) -> User:
    cursor = conn.cursor()
    query = "UPDATE users SET username = %s, email = %s, password = %s, full_name = %s, is_active = %s, is_superuser = %s, role = %s WHERE id = %s"
    cursor.execute(
        query,
        (
            user.username,
            user.email,
            user.password,
            user.full_name,
            user.is_active,
            user.is_superuser,
            user.role,
            user_id,
        ),
    )
    conn.commit()
    cursor.close()
    return user
