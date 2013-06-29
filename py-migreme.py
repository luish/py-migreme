#! /usr/bin/env python
#
# Simple script using the migre.me API
# Author: Luis Henrique Borges <contato@luishenrique.org>
# Date: 2009-10-16
#
# Usage: ./py-migreme.py <url>

from sys import argv
from urllib2 import urlopen, URLError
from xml.dom.minidom import parse


def migreme(url):
	mm_url = 'http://migre.me/api.xml?url=%s' % url

	try:
		dom = parse(urlopen(mm_url))
		if dom:
			return str(dom.getElementsByTagName('migre')[0].childNodes[0].data)

	except URLError, e:
		print 'Error: %s' % e.reason
	
	return None


def main(*args):
	list = args[0]
	if len(list) == 1:
		shortened = migreme(str(list[0]))
		if shortened:
			print 'Shortened URL:', shortened
	else:
		print "Usage: ./%s <url>" % argv[0]

	
if __name__ == "__main__":
    main(argv[1:])
