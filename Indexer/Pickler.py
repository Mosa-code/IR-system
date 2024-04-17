import pickle

# Load the inverted index from the pickle file
with open('inverted_index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)

# Print the contents of the inverted index
for term, vector in list(inverted_index.items())[:50]:
    print(f"{term}: {vector}")
    
# Load the similarity matrix from the pickle file
with open('similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Print the shape of the similarity matrix (optional)
print("Similarity Matrix Shape:", similarity_matrix.shape)

# Print the first 10 rows and columns of the similarity matrix
for row in similarity_matrix[:10]:
    print(row[:10])  # Print the first 10 elements of each row
