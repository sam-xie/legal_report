import urllib2
import bs4
from bs4 import BeautifulSoup
from util import jsonhelper


host = "www.23us.com"
param = "/html/49/49803/20035454.html"
url = "http://" + host + '/' + param

NEXT_URL_IDX_IN_FT = 2

def handle(url, target):
	resp = urllib2.urlopen(url)
	html = resp.read()
	soup = BeautifulSoup(html)

	ret = {}

	#get title
	titleCntr = soup.select("#amain h1")
	if len(titleCntr) == 0:
		print "failed: title not found"
		return 
	ret["title"] = repr(titleCntr[0].string)

	#get cnt
	cntStr = ""
	cntCntr = soup.select("#contents")
	if len(cntCntr) == 0:
		print "failed: contents not found"
		return 
	for line in cntCntr[0].stripped_strings:
		cntStr += repr(line + '\n')
	ret["cnt"] = cntStr

	#get next url
	ftLinks = soup.select("#footlink a")
	if len(ftLinks) >= NEXT_URL_IDX_IN_FT:
		ret["nextLink"] = ftLinks[NEXT_URL_IDX_IN_FT].attrs['href']

	# print ret
	return ret

if __name__ == '__main__':
	handle(url, None)