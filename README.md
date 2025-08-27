# MusicGalaxy 🎵

**MusicGalaxy** is an AI-powered music recommendation system that combines machine learning with real-time Spotify integration to deliver personalized song recommendations and synchronized lyrics display. Built with content-based filtering using the Spotify Million Song Dataset, MusicGalaxy helps users discover new music based on their preferences while providing an enhanced listening experience with automatic lyrics retrieval.

## 🚀 Features

### 🎯 Smart Music Recommendations
- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity for accurate song matching
- **Interactive Web Interface**: Streamlit-powered UI with song search and visual recommendations
- **Album Artwork Integration**: Fetches and displays high-quality album covers from Spotify API
- **Top 5 Recommendations**: Returns the most similar songs with similarity scores

### 🎤 Real-Time Lyrics Display
- **Now Playing Detection**: Automatically detects currently playing song on user's Spotify
- **Synchronized Lyrics**: Retrieves and displays lyrics in real-time using Genius API
- **Free Spotify Enhancement**: Provides lyrics access for users with free Spotify subscriptions
- **Smart Ad Handling**: Automatically pauses during Spotify advertisements

### 🔍 Advanced Song Matching
- **Natural Language Processing**: NLTK-powered text processing with Porter Stemmer
- **Case-Insensitive Search**: Robust song matching with error handling
- **Large Dataset Processing**: Efficiently handles 10,000+ song database

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Streamlit UI   │───▶│  Recommendation  │───▶│   Spotify API   │
│   (web_app.py)  │    │   Engine         │    │  (Album Art)    │
└─────────────────┘    │ (ai_mus_rec_sys) │    └─────────────────┘
                       └──────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Data Sources   │
                    │                  │
                    │ • Million Song   │
                    │   Dataset        │
                    │ • TF-IDF Matrix  │
                    │ • Cosine Sim.    │
                    └──────────────────┘

┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Lyrics Display  │───▶│  Real-time       │───▶│   Genius API    │
│ (lyrics_gen.py) │    │  Spotify Track   │    │   (Lyrics)      │
└─────────────────┘    │   Detection      │    └─────────────────┘
                       └──────────────────┘
```

## 🛠️ Technology Stack

- **Machine Learning**: scikit-learn, TF-IDF Vectorization, Cosine Similarity
- **NLP**: NLTK, Porter Stemmer
- **APIs**: Spotify Web API, Genius API
- **Web Framework**: Streamlit
- **Data Processing**: pandas, pickle
- **Authentication**: Spotify OAuth2

## 📋 Prerequisites

- Python 3.7+
- Spotify Developer Account
- Genius API Account
- Active Spotify Premium/Free Account

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/musicgalaxy.git
cd musicgalaxy
```

### 2. Install Dependencies
```bash
pip install pandas nltk scikit-learn streamlit spotipy lyricsgenius pickle
```

### 3. Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

### 4. Set Up API Credentials

#### Spotify API Setup
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new app
3. Note your `Client ID` and `Client Secret`
4. Add `https://google.com/` to redirect URIs

#### Genius API Setup
1. Go to [Genius API](https://genius.com/api-clients)
2. Create a new API client
3. Generate an access token

### 5. Configure Credentials
Update the following files with your API credentials:

**web_app.py**:
```python
spotify_client_id = "your_spotify_client_id"
spotify_client_secret = "your_spotify_client_secret"
```

**lyrics_generator.py**:
```python
spotify_client_id = "your_spotify_client_id"
spotify_client_secret = "your_spotify_client_secret"
genius_access_token = "your_genius_access_token"
```

### 6. Prepare the Dataset
```bash
# Download Spotify Million Song Dataset (spotify_millsongdata.csv)
# Place it in the project root directory
```

### 7. Train the Recommendation Model
```bash
python ai_music_rec_sys.py
```
This will generate `similarity.pkl` and `df.pkl` files.

### 8. Run Applications

#### Music Recommendation Web App
```bash
streamlit run web_app.py
```
Access at: `http://localhost:8501`

#### Real-Time Lyrics Display
```bash
python lyrics_generator.py
```

## 💻 Usage

### Music Recommendations

1. **Launch the Web App**:
   ```bash
   streamlit run web_app.py
   ```

2. **Search for Songs**:
   - Use the dropdown menu to select a song
   - Or type to search for specific tracks
   - Click "Search" to get recommendations

3. **View Results**:
   - See top 5 similar songs
   - Browse album artwork
   - Discover new music based on your selection

### Live Lyrics Display

1. **Start Spotify**: Play any song on your Spotify app

2. **Run Lyrics Generator**:
   ```bash
   python lyrics_generator.py
   ```

3. **Automatic Detection**:
   - The system detects your currently playing song
   - Lyrics appear automatically
   - Updates when you change tracks
   - Pauses during advertisements

## 🔧 How It Works

### Recommendation Algorithm

1. **Text Processing**: Song metadata is processed using NLTK and Porter Stemmer
2. **Feature Extraction**: TF-IDF vectorization creates numerical representations
3. **Similarity Calculation**: Cosine similarity finds related songs
4. **Ranking**: Results are sorted by similarity scores
5. **API Enhancement**: Spotify API adds visual elements and metadata

### Real-Time Lyrics Flow

1. **Authentication**: OAuth2 flow connects to user's Spotify account
2. **Track Detection**: Continuously monitors currently playing track
3. **Lyrics Retrieval**: Searches Genius API for matching lyrics
4. **Text Processing**: Cleans and formats lyrics for display
5. **Timing**: Synchronizes with song duration and progress

## 📁 Project Structure

```
musicgalaxy/
├── ai_music_rec_sys.py     # ML recommendation engine
├── web_app.py              # Streamlit web interface
├── lyrics_generator.py     # Real-time lyrics display
├── spotify_millsongdata.csv # Music dataset
├── similarity.pkl          # Trained similarity matrix
├── df.pkl                 # Processed dataset
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## 🎨 Features in Detail

### Music Recommendation System
- **Dataset**: 10,000 songs from Spotify Million Song Dataset
- **Algorithm**: Content-based filtering with TF-IDF and cosine similarity
- **Performance**: Sub-second recommendation generation
- **Accuracy**: High precision matching based on lyrical and metadata similarity

### Lyrics Integration
- **Real-time Detection**: Monitors Spotify playback every second
- **Error Handling**: Graceful fallback for songs without lyrics
- **Ad Detection**: Automatically handles Spotify advertisements
- **Text Cleaning**: Removes unwanted formatting and metadata

## 🚀 Future Enhancements

- [ ] **Collaborative Filtering**: Add user-based recommendations
- [ ] **Playlist Generation**: Create custom playlists from recommendations
- [ ] **Mobile App**: Native iOS/Android application
- [ ] **Social Features**: Share recommendations with friends
- [ ] **Advanced NLP**: Sentiment analysis and mood-based recommendations
- [ ] **Multi-language Support**: Lyrics in different languages
- [ ] **Offline Mode**: Cached recommendations for offline use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Spotify](https://developer.spotify.com/) for the Web API and Million Song Dataset
- [Genius](https://genius.com/) for lyrics data
- [Streamlit](https://streamlit.io/) for the web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning tools
- [NLTK](https://www.nltk.org/) for natural language processing

## ⚠️ Important Notes

### API Rate Limits
- **Spotify**: 100 requests per hour for most endpoints
- **Genius**: 1000 requests per day for lyrics retrieval
- Consider implementing caching for production use

### Privacy & Terms
- This project requires access to your Spotify listening activity
- All data processing happens locally on your machine
- No user data is stored or transmitted to third parties
- Please review Spotify and Genius API terms of service

### Dataset
- The Spotify Million Song Dataset is used for educational purposes
- Ensure you have proper licensing for commercial use
- Consider the dataset's terms and conditions

## 📞 Support

If you encounter any issues:

1. Check that all API credentials are correctly configured
2. Ensure you have an active internet connection
3. Verify that your Spotify app is running and playing music
4. Check the [Issues](https://github.com/yourusername/musicgalaxy/issues) page for common problems

For additional support, please create an issue with:
- Error messages (if any)
- Steps to reproduce the problem
- Your system configuration

---

**🎵 Enjoy discovering new music with MusicGalaxy!** 🎵
