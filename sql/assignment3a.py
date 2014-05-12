#assignment3a

import random, sqlite3

with sqlite3.connect("newnum.db") as connection:
	c=connection.cursor()
	
	c.execute("Drop table if exists numbers")
	
	c.execute("Create table numbers(num int)")
	
	for i in range(100):
		x=random.randint(0,100)
		#print(x, type(x))
		#to insert single values use a tuple format with a training comma after the variable
		c.execute('Insert into numbers Values(?)',(x,))
		