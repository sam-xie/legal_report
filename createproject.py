#!/usr/bin/python
import sys
import os
import getopt
from util import jsonhelper
from util import const
ROOT = const.ROOT
import srchandle
import spider

__PROJECT_HOME = os.path.join(ROOT, 'projects')

def doCreate(srcKey, firstUrl, name):
	print "srcKey = " + srcKey
	print "firstUrl = " + firstUrl
	print "name = " + name

	project = {}
	project['srcKey'] = srcKey
	project['firstUrl'] = firstUrl
	project['name'] = name
	host = srchandle.getSrcHost(srcKey)
	project['host'] = host
	pid = srchandle.getLastProjectId()
	project['id'] = pid
	print project

	projectPath = os.path.join(__PROJECT_HOME, pid)
	os.makedirs(projectPath)


	print projectPath

	# print spider.handle(project['host'], firstUrl, None)



def __main(argv):
	usage = 'createProject.py -s <srcKey> -u <url> -n <name>'
	srcKey = ""
	firstUrl = ""
	name = ""
	try:
		opts, args = getopt.getopt(argv,"hs:u:n:",["help", "url=","src=","name="])
	except getopt.GetoptError:
		print usage
		sys.exit(2)

	for opt, arg in opts:
		# arg = unicode(arg)
		if opt in ('-h', '--help'):
			print usage
			sys.exit()
		elif opt in ("-s", "--src"):
			srcKey = arg
		elif opt in ("-u", "--url"):
			firstUrl = arg
		elif opt in ("-n", "--name"):
			name = arg

	doCreate(srcKey, firstUrl, name)

if __name__ == '__main__':
	__main(sys.argv[1:])
