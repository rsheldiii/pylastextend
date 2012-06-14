from xml.dom.minidom import parse
dom = parse("foo.xml")
#testxml = open("test.txt", "w")
#for node in dom.getElementsByTagName('event'):  # visit every node <bar />
#    print node.toxml()
#    break
node = dom.getElementsByTagName('event')[0]
#testxml.write(node.toxml())
title = dom.getElementsByTagName('title')[0]
print title.toxml()
for artist in dom.getElementsByTagName('artist'):
    print artist.toxml()
lat = dom.getElementsByTagName('geo:lat')[0].toxml()
lon = dom.getElementsByTagName('geo:long')[0].toxml()
print (lat, lon)
