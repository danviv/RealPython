#JSON parsing 1

import json

output=json.load(open('cars.json'))

print output
print json.dumps(output, indent=4, sort_keys=True)
print output[0]["CAR"][0]["MODEL"]