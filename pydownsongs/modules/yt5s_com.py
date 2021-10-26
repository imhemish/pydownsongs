from requests import post
from json import loads

def download_module(linkofsong, inputquery, qualitylevel):
    apisite = "https://yt5s.com/"
    payload = {"q": linkofsong, "vt": "mp3"}
    postrequest = post(apisite+"api/ajaxSearch", data=payload)
    response = loads(postrequest.text)
    token = response["token"]
    vid_id = response["vid"]
    timeexp = int(response["timeExpires"])

    # Getting qualities --------
    qualities_r = response["links"]["mp3"]
    qualities = []
    for key, val in qualities_r.items():
        qualities.append(val["k"])
    qualities = list(map(int, qualities))
    qualities.sort()
    qualities.reverse()
    print(qualities)
    finalqual = {}
    if len(qualities) >= 5:
        for x in range(5):
            finalqual[x+1] = qualities[x]
    if len(qualities) < 5:
        for x in range(len(qualities)):
            finalqual[x+1] = qualities[x]
        for x in range(len(qualities)+1, 6):
            finalqual[x] = qualities[-1]
    print(finalqual)
    # -----------

    qual = finalqual[qualitylevel]
    print(qual)

    apisite = "https://backend.svcenter.xyz/api/convert"
    payload = {"v_id": vid_id, "ftype": "mp3", "fquality": qual, "token": token, "timeExpire": timeexp, "client": "yt5s.com"}
    print(payload)
    postrequest = post(apisite, data=payload)
    response = loads(postrequest.text)
    print(response)


download_module("https://www.youtube.com/watch?v=2G83yZQbg84", 4)
