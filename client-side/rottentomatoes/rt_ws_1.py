#GET data from Rotten Tomoatoes 
#Parse it and push it to local DB
#this version grabs from two endpoints: In Theatre and Box Office movies

import json
import requests
import sqlite3

KEY='get your own'

url_it=requests.get('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s'%(KEY,))


url_bo=requests.get('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=%s'%(KEY,))

binary_it=url_it.content
binary_bo=url_bo.content

output_it=json.loads(binary_it)
output_bo=json.loads(binary_bo)

movies_it=output_it['movies']
movies_bo=output_bo['movies']

with open("output.json", "wb") as outfile:
	json.dump(movies_bo,outfile)


with sqlite3.connect("movies.db") as connection:
	c=connection.cursor()
	
	for movie in movies_it:
		c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?, ?)",
		(movie["title"], movie["year"], movie["mpaa_rating"],
		movie["release_dates"]["theater"], movie["runtime"],
		movie["ratings"]["critics_score"],
		movie["ratings"]["audience_score"]))
		
	for movie in movies_bo:
		c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?, ?)",
		(movie["title"], movie["year"], movie["mpaa_rating"],
		movie["release_dates"]["theater"], movie["runtime"],
		movie["ratings"]["critics_score"],
		movie["ratings"]["audience_score"]))
		
	c.execute("SELECT * FROM new_movies ORDER BY title ASC")
	rows=c.fetchall()
	
	for r in rows:
		print r[0], r[1], r[2], r[3], r[4], r[5], r[6]
