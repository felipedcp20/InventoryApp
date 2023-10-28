from typing import List
import mysql.connector
from app.models.user import User
from app.models.item import Item


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


def delete_user(conn: mysql.connector.MySQLConnection, user_id: int) -> bool:
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    return True


def get_items(conn: mysql.connector.MySQLConnection) -> List[User]:
    cursor = conn.cursor()
    query = "SELECT * FROM items"
    cursor.execute(query)
    result = cursor.fetchall()
    items = []
    
    for item in result:
        item = Item(
        id=item[0],
        name=item[1],
        description=item[2],
        owner_id=item[3],
        )
        items.append(item)
    
    cursor.close()
    return items

def get_item(conn: mysql.connector.MySQLConnection, item_id: int) -> Item:
    cursor = conn.cursor()
    query = "SELECT * FROM items WHERE id = %s"
    cursor.execute(query, (item_id,))
    result = cursor.fetchall()
    item = Item(
        id=result[0][0],
        name=result[0][1],
        description=result[0][2],
        owner_id=result[0][3],
    )
    cursor.close()
    return item

def create_item(conn: mysql.connector.MySQLConnection, item: Item) -> Item:
    cursor = conn.cursor()
    query = "INSERT INTO items (name, description, owner_id) VALUES (%s, %s, %s)"
    cursor.execute(
        query,
        (
            item.name,
            item.description,
            item.owner_id,
        ),
    )
    conn.commit()
    cursor.close()
    return item

def update_item(conn: mysql.connector.MySQLConnection, item_id: int, item: Item) -> Item:
    cursor = conn.cursor()
    query = "UPDATE items SET name = %s, description = %s, owner_id = %s WHERE id = %s"
    cursor.execute(
        query,
        (
            item.name,
            item.description,
            item.owner_id,
            item_id,
        ),
    )
    conn.commit()
    cursor.close()
    return item

def deleted_item(conn: mysql.connector.MySQLConnection, item_id: int) -> bool:
    cursor = conn.cursor()
    query = "DELETE FROM items WHERE id = %s"
    cursor.execute(query, (item_id,))
    conn.commit()
    cursor.close()
    return True