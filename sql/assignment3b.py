#continuatioon of assignment 3a

import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c=connection.cursor()
	x={'1':'avg','2':'max','3':'min','4':'sum','5':'exit'}
	while True:
		try:
			user=int(input("Enter \n1 to find the average,\n2 to find the max,\n3 to find the min,\n4 to find the sum or 5 to exit\n"))
		except ValueError:
			print("enter an integer")
			break
		key=str(user)
		#print(key)
		if key == '5':
			print('Bye')
			break
		elif key in x:
			s='select '+x[key]+'(num) from numbers'
			#print(x[key], s)
			c.execute(s)
			out=c.fetchone()
			for row in out:
				print(x[key],row)
		
		else:
			print("Enter a number between 1 and 5: 5 to exit")