import requests
import sys

if len(sys.argv) < 3:
	print "python s3bruteforce.py http://s3.amazonaws.com/{}format wordlist"
	sys.exit(0)

wordlist = open(sys.argv[2])
data = wordlist.readlines()
wordlist.close()

for word in data:
	word=word.strip()
	req = requests.get(sys.argv[1].format(word))

	if req.status_code!=404:
		print " Found potential bucket: "+sys.argv[1].format(word)


