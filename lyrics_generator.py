# import os
# genius client id = YprDUCCA6eomDrFoDO9mH_uUEyjW_4UQmKj1wh11gOH2AUFXpIMy_ecrbhKABavf
# genius client secret = jHcgN3sKK01xhzHMCcTArMqnBYDo_fslMnO3WRsnI_5CuvNYVfszHinnz8L6tgyGsXodifK9aBMaj8lgc0PGeA
import json

"""
TO DO:
        Deal with play next or previous
        Get rid of non-lyrics display if possible
"""

import time
import re
import spotipy
import lyricsgenius as lg

spotify_client_id = "e8ff6b9e55494f64b97a3c5ce3c7c0c2"
spotify_client_secret = "aef908a3ccc94c39a72de987db53fa9b"
spotify_redirect_uri = "https://google.com/"
genius_access_token = "AXfaK0cpkiQ5E8N1wYtm1LSQZu94ETj1vSlj4pGsnrKrocMPmvpn-Mjs3ZHM0DSa"

scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_client_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

# spotify object
spotify_object = spotipy.Spotify(auth=token)

# genius object
genius = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()
print(json.dumps(current, sort_keys=False, indent=4))


while True:
    current = spotify_object.currently_playing()
    status = current['currently_playing_type']

    if status == 'track':
        artist_name = current['item']['album']['artists'][0]['name']
        song_title = current['item']['name']
        length = current['item']['duration_ms']
        progress = current['progress_ms']
        time_left = int((length - progress) / 1000)
        song = genius.search_song(title=song_title, artist=artist_name)

        if song is not None:
            lyrics = song.lyrics
            lyrics = re.sub(r'Embed|7Embed', '', lyrics)
            expected_lyrics = str(song_title) + " " + "Lyrics"
            if expected_lyrics in lyrics:
                print(lyrics)
            else:
                print("Looks like we do not have the lyrics for", song_title, "by", artist_name)

        time.sleep(time_left)

    elif status == 'ad':
        time.sleep(30)
