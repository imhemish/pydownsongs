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

			# Modules reside in modules directory ------
			print("Transferring control to youtube_dl")
			from pydownsongs.modules.youtube_dl_module import download_module
			download_module(linkofsong, inputquery, qualitylevel)
			# -------------------------

			# Adding metadata -------------------
			pydownsongs.add_meta(pydownsongs.get_meta(inputquery.title()), (inputquery.title()+".mp3"))
			# ----------------
			
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