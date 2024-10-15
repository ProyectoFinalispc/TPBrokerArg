import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host='localhost',
                    database='arg_broker',
                    user='root',
                    password='%clavesql%',
                    port = '3307'
                )
            except Error as e:
                print(f"Error al conectar con la base de datos: {e}")
                self.connection = None
        return self.connection

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
