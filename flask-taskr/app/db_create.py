#db_create.py

import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c=connection.cursor()
	
	c.execute("""CREATE TABLE ftasks(taskid INTEGER\
	PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
	
	#dummy data
	c.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish this tutorial","14/05/2014",10,1)')
	
	c.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish Real Python 2 Course","14/06/2014",10,1)')