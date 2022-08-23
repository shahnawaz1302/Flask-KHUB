
import sqlite3
from flask_restful import Resource,reqparse
class User:
    def __init__(self, _id, username, password):
        self.id =_id
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
            # user=cls(row[0],row[1],row[2])
            user=cls(*row)
        else:
            user=None
        
        connection.close()
        
        return user
    @classmethod
    def find_by_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(_id,))
        row=result.fetchone()
        if row:
            # user=cls(row[0],row[1],row[2])
            user=cls(*row)
        else:
            user=None
        
        connection.close()
        return user
class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cant be empty')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cant be empty'
                        )
    def post(self):
        # below line helps us to pass the arguements
        data=UserRegister.parser.parse_args()
        # this wil help us to eradicate the duplicate users in database to register twice
        if User.find_by_username(data['username']):
            return {"message":"A user with that username alreaady exixts"},400
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        # Below will help us to insert the values 
        query="INSERT INTO users VALUES (NULL,?,?)"
        # Inserting the username and password
        cursor.execute(query,(data['username'],data['password']))
        connection.commit()
        connection.close()
        return {"message":"User created sucessfully"},201    