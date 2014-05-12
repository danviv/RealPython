#JOIN

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	
	#create a dictionary of sql queries
	sql={'average':"select avg(population) from population",\
	'maximum':'select max(population) from population',\
	'minimum':'select min(population) from population',\
	'sum':'select sum(population) from population',\
	'count':'select region, count(*) from population, regions where population.city=regions.city group by regions.region'}
	
	for keys, values in sql.items():
		c.execute(values)
		
		
		r=c.fetchall()
		print(keys+',',r)
