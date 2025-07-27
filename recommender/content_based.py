import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, csv_path):
        self.books = pd.read_csv(csv_path)
        self.vectorizer = TfidfVectorizer()
        self._prepare()

    def _prepare(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.books['description'])

    def recommend(self, title, top_n=3):
        if title not in self.books['title'].values:
            print("Book not found.")
            return []

        idx = self.books[self.books['title'] == title].index[0]
        cosine_sim = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]

        return self.books['title'].iloc[similar_indices].tolist()
