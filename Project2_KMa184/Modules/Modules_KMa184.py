# similarity_module.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to compute tag-based similarity
def compute_tag_similarity(tags_df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(tags_df['tag'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

