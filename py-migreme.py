#! /usr/bin/env python
#
# Simple script using the migre.me API
# Author: Luis Henrique B. Sousa <contato@luishenrique.org>
# Date: 2009-10-16
#
# Usage: python migreme.py <url>
# Example: ./migreme.py http://twitter.com/luish_
#	

from sys import argv
import urllib
import xml.dom.minidom

api = 'http://migre.me/api.xml?url=%s'

def migreme(url):
	mm_url = api % url
	dom = xml.dom.minidom.parse(urllib.urlopen(mm_url))

	return str(dom.getElementsByTagName('migre')[0].childNodes[0].data)

def main(*args):
	list = args[0]
	if len(list) == 1:
		print '\n-> Shortened URL:', migreme(str(list[0]))
	else:
		print """
- It works only with a URL.
- Usage: ./%s <url>
""" % argv[0]
	
if __name__ == "__main__":
    main(argv[1:])
