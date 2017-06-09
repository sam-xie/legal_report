import urllib2
import bs4
import re
from bs4 import BeautifulSoup
from util import jsonhelper


REGEX_HTTP_HEAD = r"https?://"
DEF_HTTP_HEAD = r"http://"

NEXT_URL_IDX_IN_FT = 2

def handle(host, query, target):
	print re.match(REGEX_HTTP_HEAD, host)
	if None == re.match(REGEX_HTTP_HEAD, host):
		host = DEF_HTTP_HEAD + host
	resp = urllib2.urlopen(host + '/' + query)
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
