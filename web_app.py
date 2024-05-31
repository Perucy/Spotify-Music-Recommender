import streamlit as st
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


spotify_client_id = "e8ff6b9e55494f64b97a3c5ce3c7c0c2"
spotify_client_secret = "aef908a3ccc94c39a72de987db53fa9b"
spotify_redirect_uri = "https://google.com/"

client_cred_manager = SpotifyClientCredentials(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_cred_manager)


music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def get_song_album_pic(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=query, type="track")

    if results and results['tracks']['items']:
        track = results['tracks']['items'][0]
        album_pic_url = track['album']['images'][0]['url']
        return album_pic_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommend_song(song_name):
    idx = music[music['song'] == song_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommended_songs = []
    recommended_song_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_song_posters.append(get_song_album_pic(music.iloc[i[0]].song, artist))
        recommended_songs.append(music.iloc[i[0]].song)

    return recommended_songs, recommended_song_posters


st.title('MusicGalaxy')


song_list = music['song'].values
selected_song = st.selectbox('Type or Select a song from the dropdown menu',
                             song_list)

if st.button('Search'):
    recommended_song, recommended_song_poster = recommend_song(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_song[0])
        st.image(recommended_song_poster[0])
    with col2:
        st.text(recommended_song[1])
        st.image(recommended_song_poster[1])
    with col3:
        st.text(recommended_song[2])
        st.image(recommended_song_poster[2])
    with col4:
        st.text(recommended_song[3])
        st.image(recommended_song_poster[3])
    with col5:
        st.text(recommended_song[4])
        st.image(recommended_song_poster[4])
