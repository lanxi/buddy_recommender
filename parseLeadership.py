import os
import sys
from parseHTML import parseHTML

path = '/Users/lanxihuang/buddy/data/leadership/'

for fileName in os.listdir(path):
	if fileName != '.DS_Store':
		HTMLfile = open(path+fileName, 'rU')
		try:
			parseHTML(HTMLfile, fileName)
		except:
			e = sys.exc_info()[0]
			print ( "<p>Error: %s</p>" % e )
