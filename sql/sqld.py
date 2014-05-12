# UPDATE and DELETE commands

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	
	c.execute("UPDATE population SET population=9000000 where city='New York City'")
	
	c.execute("DELETE FROM population where city='Boston'")
	
	print("new DATA")
	c.execute("SELECT * FROM population")
	
	rows=c.fetchall()
	
	for r in rows:
		print(r[0],r[1],r[2])
	
