#XML parsing

from xml.etree import ElementTree as et

doc=et.parse("cars.xml")

print doc.find("CAR/MODEL").text

for element in doc.findall("CAR"):
	print (element.find("MAKE").text+" "+
			element.find("MODEL").text+
			", $"+element.find("COST").text)