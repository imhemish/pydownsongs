import sys
from ytmusicapi import YTMusic as ytmapi
import music_tag
import requests
import pydownsongs
from os.path import expanduser, join

randusrheaders = {"User-Agent": pydownsongs.randomUsrAgent()}

ytm = ytmapi()
def raw_query(query):
    raw_data = ytm.search(query)
    found_result = None
    for item in raw_data:
        if item["resultType"] == "song":
            found_result = item
            break
        else:
            pass
    if found_result == None:
        for item in raw_data:
            if item["resultType"] == "video":
                found_result = item
                break
            else:
                pass
    return found_result

def encode_pydownsongs(raw_query):
    final_return = {}
    final_return["title"] = raw_query["title"]
    final_return["album"] = raw_query["album"]["name"]
    if raw_query["year"] != None:
        final_return["year"] = raw_query["year"]
    artists_list = []
    for artist in raw_query["artists"]:
        artists_list.append(artist["name"])
        
    def doesnt_contain_song_artist(string):
        if "song" in string.lower():
            return False
        else:
            return True
    artists_list = list(filter(doesnt_contain_song_artist, artists_list))
    final_return["artists"] = artists_list
    final_return["thumbnail"] = raw_query["thumbnails"][-1]["url"]
    return final_return

def get_meta(term): # Combines previous two functions into one
    print("Getting metadata")
    return encode_pydownsongs(raw_query(term))

def add_meta(pydownsongs_encoded_dict, filepath):
    print("Adding metadata to file")
    f = music_tag.load_file(filepath)
    f['title'] = pydownsongs_encoded_dict['title']
    print("Added title: {}".format(pydownsongs_encoded_dict['title']))
    f['album'] = pydownsongs_encoded_dict['album']
    print("Added album: {}".format(pydownsongs_encoded_dict['album']))
    f['artist'] = pydownsongs_encoded_dict['artists']
    print("Added artists: {}".format(pydownsongs_encoded_dict['artists']))
    try:
        f['year'] = pydownsongs_encoded_dict['year']
        print("Added year: {}".format(pydownsongs_encoded_dict['year']))
    except:
        pass
    r = requests.get(pydownsongs_encoded_dict['thumbnail'], allow_redirects=True, headers=randusrheaders)
    f['artwork'] = r.content
    print("Added thumbnail")
    f.save()