#sql qith csv file

import sqlite3, csv

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	employees = csv.reader(open("employees.csv",'r'))
	
	#c.execute("CREATE TABLE employees(firstname, lastname)")
	try:
		c.executemany("INSERT INTO employee VALUES(?,?)",employees)
	except sqlite3.OperationalError as e:
		print("Operation failed with error:",e)
	
	alist=c.execute("SELECT * FROM employees")
	for row in alist:
		print(row)
		
	c.execute("SELECT * FROM employees")	
	alist2=c.fetchall()
	print("alist2 is :",alist2)
	for r in alist2:
		print(r[0],r[1])
	

