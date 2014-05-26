#GET data from Rotten Tomoatoes 
#Parse it and push it to local DB

import json
import requests
import sqlite3

KEY='<get your own>'

url=requests.get('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s'%(KEY,))


binary=url.content


output=json.loads(binary)
print output
movies=output['movies']


with open("output.json", "wb") as outfile:
	json.dump(output,outfile)


with sqlite3.connect("movies.db") as connection:
	c=connection.cursor()
	
	for movie in movies:
		c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?, ?)",
		(movie["title"], movie["year"], movie["mpaa_rating"],
		movie["release_dates"]["theater"], movie["runtime"],
		movie["ratings"]["critics_score"],
		movie["ratings"]["audience_score"]))
		
	c.execute("SELECT * FROM new_movies ORDER BY title ASC")
	rows=c.fetchall()
	
	for r in rows:
		print r[0], r[1], r[2], r[3], r[4], r[5], r[6]
