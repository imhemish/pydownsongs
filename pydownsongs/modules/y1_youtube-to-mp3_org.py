import bs4
import pydownsongs

def download_module(linkofsong, inputquery, qualitylevel) 
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
	pydownsongs.others.download_function(finallink, inputquery)