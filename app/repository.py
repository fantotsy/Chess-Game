import mysql.connector

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
SCHEMA = 'chess'


class Repository(object):

    def __init__(self):
        self.connection = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD, database=SCHEMA, raise_on_warnings=True)

    def save_game(self, name, activity):
        cursor = self.connection.cursor()
        sql = "INSERT INTO games (name, activity) VALUES (%s, %s)"
        values = (name, activity)
        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()
