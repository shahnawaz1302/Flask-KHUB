# In this we are creating a table and giving certain values in it and we are using those values into the postman authentication
from select import select
import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
create_table="CREATE TABLE users(id int,username text,password text)"
cursor.execute(create_table)
user=(1,'nawaz','abcdf')
insert_table=" INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_table,user)
many=[
    (2,'eazaz','hsdfh'),
    (3,'azzu','dsgfu')
]
cursor.executemany(insert_table,many)
selecty_table='SELECT * FROM users'
for row in cursor.execute(selecty_table):
    print(row)
connection.commit()
connection.close()