
import mysql.connector
from fastapi import HTTPException

class Dao:

    def __init__(self) -> None:
        try:
            self.dbaas_conn = self.connect_to_db()
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error to connecting to MySQL: {err}")

    def connect_to_db(self) -> mysql.connector.MySQLConnection:
        """
        Connect to the MySQL database.
        Returns: MySQLConnection, the connection to the MySQL database.
        """
        return mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            port="3306",
            database="inventory",
        )
