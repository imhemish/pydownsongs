import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pydownsongs
import toml
from os.path import expanduser, join, exists
from os import getcwd, remove
import os
import sys

def dl_spotlist(PlaylistUrl, qualitylevel):
    # Spotipy saves a .cache file for secrets
    if exists(join(getcwd(), ".cache")):
        print("Sorry, current directory already contains a .cache node, thus download is not possible in this directory (most probably you are in your home directory. Please navigate to some other directory and then perform the operation.")
        sys.exit()
    
    print("{} in quality {}".format(PlaylistUrl, qualitylevel))
    pydownsongs.createDirIfNotExists(join(expanduser("~"), ".config"))
    config_file = join(expanduser("~"), ".config", "pydownsongs.toml")
    
    if not exists(config_file):
        print("You haven't set your spotify secrets")
        print("Exiting")
        sys.exit()
    try:
        config = toml.load(config_file)
        spotid = config["id"]
        spotsecrets = config["secrets"]
        print("Your spotify id: {}".format(spotid))
        print("Your spotify secret: {}".format(spotsecrets))
    except:
        print("There was some error in your spotify secrets")
        print("Exiting")
        sys.exit()

    try:
        if PlaylistUrl[0]=='h':
            Url = PlaylistUrl[34:]
        elif PlaylistUrl[0]=='o':
            Url = PlaylistUrl[26:]
        else:
            Url = PlaylistUrl

        if(len(Url)>22):
            Url = Url[:22]

        auth_manager = SpotifyClientCredentials(client_id = spotid , client_secret = spotsecrets)

        sp = spotipy.Spotify(auth_manager = auth_manager)

        def getTrackIDs (user, playlist_id):
            track_ids = []
            playlist = sp.user_playlist(user, playlist_id)
            for item in playlist['tracks']['items']:
                track = item['track']
                track_ids.append(track['id'])
            return track_ids

        track_ids = getTrackIDs('spotify', Url)

        def TrackFeature(id):
            track_info = sp.track(id)
            name = track_info['name']
            artist = track_info['album']['artists'][0]['name']
            name_artist = name + " " + artist
            return name_artist

        final_array = []

        for i in range(len(track_ids)):
            s = TrackFeature(track_ids[i])
            final_array.append(s)
    
    except Exception as e:
        print(e)
        print("Some error occured")
    finally:
        try:
            remove(".cache")
        except:
            try:
                remove(".cache.")
            except:
                pass

    pydownsongs.downloadarray(final_array,qualitylevel)

    try:
        remove(".cache")
    except:
        try:
            remove(".cache.")
        except:
            pass
    
