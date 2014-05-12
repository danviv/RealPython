#Create sqlite3 dba and table

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	try:
		c.execute("""CREATE TABLE regions(city TEXT,region TEXT)""")
	except sqlite3.OperationalError:
	
	#insert multiple records using a tuple
	cities = (\
	('New York City', 'Northeast'),
	('San Francisco', 'West'),
	('Chicago', 'Midwest'),
	('Houston', 'South'),
	('Phoenix', 'West'),
	('Boston', 'Northeast'),
	('Los Angeles', 'West'),
	('Houston', 'South'),
	('Philadelphia', 'Northeast'),
	('San Antonio', 'South'),
	('San Diego', 'West'),
	('Dallas', 'South'),
	('San Jose', 'West'),
	('Jacksonville', 'South'),
	('Indianapolis', 'Midwest'),
	('Austin', 'South'),
	('Detroit', 'Midwest')
	)
	
	#print(cities)
	c.executemany('INSERT INTO regions  VALUES(?,?)',cities)

c.execute('SELECT * from regions ORDER by region ASC')
for row in c.fetchall():
	print(row[0],row[1])