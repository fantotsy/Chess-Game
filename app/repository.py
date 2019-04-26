import mysql.connector
import datetime

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
SCHEMA = 'chess'


class Repository(object):

    def __init__(self):
        self.connection = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD, database=SCHEMA, raise_on_warnings=True)

    def save_game(self, name, activity):
        cursor = self.connection.cursor()
        sql = "INSERT INTO games (name, activity, date) VALUES (%s, %s, %s)"
        values = (name, activity, datetime.datetime.now())
        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()

    def get_game(self, name):
        cursor = self.connection.cursor()
        sql = "SELECT activity FROM games WHERE name = %s"
        value = (name,)
        cursor.execute(sql, value)
        game_activity = cursor.fetchone()
        cursor.close()
        return game_activity

    def get_games(self):
        cursor = self.connection.cursor()
        sql = "SELECT name, date FROM games"
        cursor.execute(sql)
        games = cursor.fetchall()
        cursor.close()
        return games
