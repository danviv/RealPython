#Google direction API

import json, requests
url="http://maps.googleapis.com/maps/api/directions/json?origin=Edinburgh&destination=Glasgow&Sensor=false&mode=walking"

data=requests.get(url)
binary=data.content
output=json.loads(binary)
#print output
print output['status']
#print output['routes']

for route in output['routes']:
	for leg in route['legs']:
		for step in leg['steps']:
			print step['html_instructions']
