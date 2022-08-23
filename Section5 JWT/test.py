import sqlite3
# This will establish the connection of sqlite3 and along with we are going to create a database eg:data.db
connection=sqlite3.connect('data.db')
# We are required to activate the cursor with the help of the variable whre we are established the connection in our case it is connection variable
cursor=connection.cursor()
# we are going to create the table and writr what all the components are to be present in it
create_table="CREATE TABLE users(id int,username text, password text)"
# we are going to send the above statment into the database
cursor.execute(create_table)
# Now assigning the values
user=(1,'nawaz','abcd')
# We are goint to insert the values into the table whivh we  are created
insert_query="INSERT INTO users VALUES(?,?,?)"
# Again we are goint to insert into the statment into our database
cursor.execute(insert_query,user)
bhai=[
    (2,'shan','ghij'),
    (3,'bhai','oooo')
]
cursor.executemany(insert_query,bhai)
select_query="SELECT * FROM users"
# we are selecteing all the parameters in the table and all the attributes are prresent in select_query variable
for row in cursor.execute(select_query):
    print (row)
connection.commit()
connection.close()
