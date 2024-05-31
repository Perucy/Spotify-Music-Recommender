Written by: Perucy Mussiba
Files: web_app.py, ai_mus_rec_sys.py and lyrics_generator.py
Purpose: A music recommendation system using the Spotify Million Song Dataset and Spotify API AND a lyrics-retrieving program 

ai_mus_rec_sys.py: 
  Libraries: Sklearn, NLTK, Pickle, Pandas
  The file contains an implementation of the recommendation system that utilizes the library above to retrieve the user's input song
  search through the database, match the songs and then return the top match songs

web_app.py:
  Libraries: Spotipy, Streamlit, Pickle
  The file contains a front-end implementation of a web application using Streamlit that interacts with a user to retrieve the user input song
  then interact with ai_mus_rec_sys.py to look through the database that returns the top match songs
  The program gets the top 5 match songs together with their album pictures and displays the content to the user of the recommended songs

lyrics_generator.py:
  Libraries: Spotipy, re, time, lyricsgenius
  The file contains an implementation of a program that determines the current song playing on a user's Spotify application and then it utilizes
  lyricsgenius API to retrieve the lyrics and display the lyrics to the user. This program helps the user with a free Spotify subscription to
  view the lyrics of any song without limitations
