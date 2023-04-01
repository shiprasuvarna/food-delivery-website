import sqlite3  
  
con = sqlite3.connect("foodapp.db")  
print("Database opened successfully")  
  
con.execute("create table Customer (email TEXT UNIQUE NOT NULL PRIMARY KEY, password TEXT UNIQUE)")  
  
print("Table created successfully")  
  
con.close()