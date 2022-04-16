from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .csv_handler import load_column_from_dataset

def filter_by_similarity(key):
    similar_values = []
    for value in load_column_from_dataset('Values'):
        similarity_ratio = calculate_similarity(key, value)
        if similarity_ratio > 50:
            similar_values.append(
                {
                    "value": value,
                    "ratio": similarity_ratio
                }
            )
    return similar_values

def calculate_similarity(first_text, second_text):
    vectorizer = TfidfVectorizer()
    embeddings = vectorizer.fit_transform([first_text, second_text])
    similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()
    return similarities[0] * 100