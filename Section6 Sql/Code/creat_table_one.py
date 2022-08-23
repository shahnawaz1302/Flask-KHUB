# In this we are creating a table and registering the values into it and it is going to save the values we enter into the databse
import sqlite3

connection=sqlite3.connect('data.db')

cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"

cursor.execute(create_table)

create_table="CREATE TABLE IF NOT EXISTS items(name text,price real)"

cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES('mohammed',20.45)")

connection.commit()

connection.close()
