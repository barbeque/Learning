collection = {
	"cars": [
		{ "name": "subaru impreza", "year": 2006, "mileage": 127000 },
		{ "name": "porsche 911", "year": 1993, "mileage": 162040 },
	],
	"games": [
		{ "name": "super mario bros", "platform": "NES" }
	]
}

# crappy recursive hashtable to xml producer
def dictToXml(root):
	xml = ''
	for key in root.keys():
		if isinstance(root[key], dict):
			# recurse
			xml += '<%s>\n%s</%s>\n' % (key, dictToXml(root[key]), key)
		elif isinstance(root[key], list):
			xml += '<%s>\n' % key
			for item in root[key]:
				xml += '<%s>\n' % depluralize(key)
				xml += '%s' % dictToXml(item)
				xml += '</%s>\n' % depluralize(key)
			xml += '</%s>\n' % key
		else:
			value = root[key]
			xml += '<%s>%s</%s>\n' % (key, value, key)
	return xml

def depluralize(name):
	return name.rstrip('s') # TODO: low-rent

print dictToXml(collection)