import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv("spotify_millsongdata.csv")
df = df.sample(10000).drop('link', axis=1).reset_index(drop=True)

# df['text'] = df['text'].str.lower().replace(r'^\w\s', ' ').str.replace(r'\n', ' ', regex=True)
# print(df['text'][0])
stemmer = PorterStemmer()


def token(txt):
    token_word = nltk.word_tokenize(txt)
    a = [stemmer.stem(w) for w in token_word]
    return " ".join(a)


df['text'].apply(lambda x: token(x))

tfid = TfidfVectorizer(analyzer='word', stop_words='english')
matrix = tfid.fit_transform(df['text'])
similar = cosine_similarity(matrix)


def recommender(song_name):
    try:
        # Case insensitive matching and stripping whitespaces
        idx = df[df['song'].str.strip().str.lower() == song_name.strip().lower()].index[0]
    except IndexError:
        print(f"Song '{song_name}' not found in the database.")
        return []

    distance = sorted(list(enumerate(similar[idx])), reverse=True, key=lambda x: x[1])
    song = []
    for s_id in distance[1:5]:
        song.append(df.iloc[s_id[0]].song)
    return song


pickle.dump(similar, open("similarity.pkl", "wb"))
pickle.dump(df, open("df.pkl", "wb"))

