#XML parsing 3

from xml.etree import ElementTree as et
import requests
xml=requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

with open("test.xml","wb") as code:
	code.write(xml.content)
	
doc=et.parse("test.xml")

for element in doc.findall("CD"):
	print "Album: ", element.find("TITLE").text
	print "Artist: ", element.find("ARTIST").text
	print "Year: ", element.find("YEAR").text,"\n"