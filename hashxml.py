collection = {
	"cars": [
		{ "name": "subaru impreza", "year": 2006, "mileage": 127000 },
		{ "name": "porsche 911", "year": 1993, "mileage": 162040 },
	],
	"games": [
		{ "name": "super mario bros", "platform": "NES" }
	]
}

def dictToXml(root):
	xml = ''
	for key in root.keys():
		if isinstance(root[key], dict):
			# recurse
			xml = '%s<%s>\n%s</%s>\n' % (xml, key, dictToXml(root[key]), key)
		elif isinstance(root[key], list):
			xml = '%s<%s>' % (xml, key)
			for item in root[key]:
				xml = '%s%s' % (xml, dictToXml(item))
			xml = '%s</%s>' % (xml, key)
		else:
			value = root[key]
			xml = '%s<%s>%s</%s>\n' % (xml, key, value, key)
	return xml

print dictToXml(collection)