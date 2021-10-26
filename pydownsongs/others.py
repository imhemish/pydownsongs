import random
import requests # pip install requests
import bs4 # pip install bs4
import os
import googlesearch # pip install google
import sys
import time
import pydownsongs

# Create directory if doesn't exist ---
def createDirIfNotExists(path):
		if os.path.exists(str(path)) == False:
			os.mkdir(str(path))
		else:
			pass
# -------------------------------------

# Random User Agent ------------------
def randomUsrAgent():
	try:
		if not os.path.exists(os.path.join(os.path.expanduser("~"), ".cache", "randomUsrAgent.txt")):
		    getreq = requests.get("https://raw.githubusercontent.com/tamimibrahim17/List-of-user-agents/master/Chrome.txt")
		    uastrings = getreq.text
		    with open((os.path.join(os.path.expanduser("~"), ".cache" "randomUsrAgent.txt")), "w")  as file:
		    	file.write("\n".join((uastrings.split("\n")[2:])))
		else:
			uastrings = open((os.path.join(os.path.expanduser("~"), ".cache" "randomUsrAgent.txt")), "r").read().split("\n")[2:]
		return random.choice(uastrings)
	except:
		return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# -------------------------------------

# ping --------------------------------
def ping(url):
	try:
		rand = str(randomUsrAgent())
		usr_agent = {'User-Agent': rand}
		requestget = requests.get(url, headers=usr_agent)
		if requestget.status_code == 200:
			return True
		else:
			return False
	except:
		print("{} not available".format(url))
		return False
# -------------------------------------

def checkInternet(): # Check Internet ------------------
	print("Checking Internet Connection...")
	time.sleep(0.2)
	if ping("https://www.google.com/") == True:
		print("Internet connection is available.")
	else:
		print("It seems that Internet is not available. Please try again.")
		sys.exit()
# ---------------------------------------------------

# Implementation of googlesearch -------
def gSearch(term):
	searchreq = list(googlesearch.search(term, stop=10, num=10, user_agent=(str(randomUsrAgent()))))
	return searchreq
# -------------------------------------

# Download function made for modular functions (optional)
def download_function(finallink, inputquery):
	print("Downloading " + finallink + " as "+inputquery.title()+".mp3")
	randusrheaders = {"User-Agent": pydownsongs.others.randomUsrAgent()}
	with open((inputquery.title()+".mp3"), "ab") as downloadfile:
		r = requests.get(finallink, allow_redirects=True, headers=randusrheaders)
		downloadfile.write(r.content)
