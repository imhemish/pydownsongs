# imports ------------------------------
import requests #pip install requests
import pydownsongs
import bs4 # pip install bs4
#----------------------------------------

# Main song downloading function -----------------------------------
def download(songname, qualitylevel):
	while True:
		try:
			inputquery = str(songname)
			if inputquery == "":
			    break
			listoflinks = pydownsongs.others.gSearch(str(inputquery + " song" + " youtube"))
			linkofsong = listoflinks[0]
			while not "www.youtube.com" in listoflinks[0]:
				linkofsong = listoflinks[1]
				listoflinks.pop(0)
			print(inputquery)
			print(linkofsong)
			apisite = "https://y1.youtube-to-mp3.org/searchdl.php"
			payload = {"url": linkofsong,
			"type": "mp3"}
			postrequest = requests.post(apisite, data = payload)
			responsehtml = postrequest.text
			bs = bs4.BeautifulSoup(responsehtml, 'html.parser')
			table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="tab_mp3") 
			rows = table.findAll(lambda tag: tag.name=='tr')
			for y in [1,2,3,4,5]:
			    if str(y) == str(qualitylevel):
			        myrequirement = str(rows[y])
			hrefstring = myrequirement.find('href="')
			requiredhrefstartstring = str((int(hrefstring) + 6))
			requiredhrefstopstring = (int(myrequirement.find('" onclick="ads()"')))
			finallink = (myrequirement[int(requiredhrefstartstring):int(requiredhrefstopstring)])
			print("Downloading " + finallink + " as "+inputquery.title()+".mp3")
			randusrheaders = {"User-Agent": pydownsongs.others.randomUsrAgent()}
			with open((inputquery.title()+".mp3"), "ab") as downloadfile:
				r = requests.get(finallink, allow_redirects=True, headers=randusrheaders)
				downloadfile.write(r.content)
			pydownsongs.add_meta(pydownsongs.get_meta(inputquery.title()), (inputquery.title()+".mp3"))
			break
		except Exception as e:
			print("Some error occured")
			print(e)
			with open("failedtemp.txt", "a") as failedfile:
				failedfile.write(str(songname)+"\n")
			break
# -------------------------------------------------------------------


# Download array of songs -------------
def downloadarray(array, qualitylevel):
	for item in array:
		download(item, qualitylevel)
# ---------------------