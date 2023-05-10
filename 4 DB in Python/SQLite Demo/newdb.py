'''
This code is a demo of how to create a database with a schema structure in Python using SQL Lite.
For more information, see: https://datatofish.com/create-database-python-using-sqlite3/ 
'''
import sqlite3
#we can name the file antyhing we want, but it is common to use .db
db_file = "new.db"

#the connection is the database file itself represented in python
connection = sqlite3.connect(db_file)

#the cursor is the object that will allow us to execute SQL commands
cursor = connection.cursor()

#execute runs the SQL command but does not save it, the results are just in memory for now
cursor.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
          
cursor.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
#commit is when we actually save the changes we made to the database            
connection.commit()