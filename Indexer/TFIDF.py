from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pickle

directory = "./TestDocuments"

documents = []
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
        documents.append(f.read())

vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Create a dictionary mapping terms to their tf-idf vectors
inverted_index = {term: tfidf_matrix.getcol(idx).toarray().ravel().tolist() for term, idx in vectorizer.vocabulary_.items()}

# Print the first 10 items of the inverted index
for i, (term, vector) in enumerate(inverted_index.items()):
    if i >= 10:
        break
    print(f"{term}: {vector}")

# Save the inverted index in pickle format
with open('inverted_index.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)

# Calculate cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save the similarity matrix in pickle format
with open('similarity_matrix.pkl', 'wb') as f:
    pickle.dump(similarity_matrix, f)

