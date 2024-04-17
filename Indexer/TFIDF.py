from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pickle

directory = "./TestDocuments"

documents = []
for filename in os.listdir(directory):
    try:
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            documents.append(f.read())
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

if not documents:
    print("No documents found in the directory.")
    exit()

vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Create a dictionary mapping terms to their tf-idf vectors
inverted_index = {term: tfidf_matrix.getcol(idx).toarray().ravel().tolist() for term, idx in vectorizer.vocabulary_.items()}

# Save the inverted index in pickle format
with open('inverted_index.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)

# Calculate cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save the similarity matrix in pickle format
with open('similarity_matrix.pkl', 'wb') as f:
    pickle.dump(similarity_matrix, f)

print("Indexing completed successfully.")
