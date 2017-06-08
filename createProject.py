#!/usr/bin/python
from util import jsonhelper
import sys
import getopt

def main(argv):
	usage = 'createProject.py -s <srcKey> -u <url> -n <name>'
	srcKey = ""
	firstUrl = ""
	name = ""
	try:
		opts, args = getopt.getopt(argv,"hs:u:n:",["url=","src=","name="])
	except getopt.GetoptError:
		print usage
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print usage
			sys.exit()
		elif opt in ("-s", "--src"):
			srcKey = arg
		elif opt in ("-u", "--url"):
			firstUrl = arg
		elif opt in ("-n", "--name"):
			name = arg

	print "srcKey = " + srcKey
	print "firstUrl = " + firstUrl
	print "name = " + name

if __name__ == '__main__':
	main()
