from sklearn.feature_extraction.text import CountVectorizer
import os
import re
import pandas as pd
import pickle

directory = "./TestDocuments"

# Read the content of each HTML file and store it in a list along with the document name
documents = []
doc_names = []

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        doc_name = re.sub(r'\.html$', '', filename)  # Remove ".html" extension
        doc_names.append(doc_name)
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            documents.append((doc_name, f.read()))

# Initialize a CountVectorizer to generate the term-document matrix
vectorizer = CountVectorizer()

# Extract the document texts from the list
texts = [text for _, text in documents]

# Fit and transform the documents to get the term-document matrix
term_doc_matrix = vectorizer.fit_transform(texts)

# Transpose the term-document matrix to match the expected shape for DataFrame creation
transposed_matrix = term_doc_matrix.transpose()

# Create a DataFrame for the posting list
terms = vectorizer.get_feature_names_out()
posting_df = pd.DataFrame(transposed_matrix.toarray(), columns=doc_names, index=terms)

# Save the posting list DataFrame in pickle format
with open('posting_list_df.pkl', 'wb') as f:
    pickle.dump(posting_df, f)

print("Posting list created and saved as posting_list_df.pkl")
