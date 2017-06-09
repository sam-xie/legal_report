#!/usr/bin/python
import sys
import getopt
from util import jsonhelper
from util import const
ROOT = const.ROOT

__DATA_FILE_PATH = ROOT + '/srcdata.json'
__srcData = None

def loadData():
	return jsonhelper.load(__DATA_FILE_PATH)
def saveData():
	jsonhelper.save(__DATA_FILE_PATH, __srcData)

def __initData():
	global __srcData
	__srcData = loadData()

def __main(argv):
	print "src list:"
	for (k, v) in __srcData['novels'].items():
		print k, v


def getSrcHost(key):
	return __srcData and __srcData['novels'][key]['host']

def getLastProjectId():
	pid = __srcData.get('lastProjectId', 1)
	__srcData['lastProjectId'] = pid + 1
	saveData()
	return str(pid)


__initData()
if __name__ == '__main__':
	__main(sys.argv[1:])
