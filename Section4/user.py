from itertools import combinations
from multiprocessing import connection
import sqlite3
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(cls,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE username=?"
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        connection.close()
        return user
    def find_by_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(id,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        connection.close()
        return user