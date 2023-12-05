import mysql.connector

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = self.config

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self):
        pass
