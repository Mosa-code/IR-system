import pickle

with open('posting_list_df.pkl', 'rb') as f:
    data = pickle.load(f)
    for term, doc_list_indices in list(data.items())[:10]:
        doc_list = [doc_name for idx, doc_name in enumerate(data.columns) if doc_list_indices[idx] == 1]
        term_encoded = term.encode('utf-8', errors='replace').decode('utf-8')
        doc_list_encoded = [doc.encode('utf-8', errors='replace').decode('utf-8') for doc in doc_list]
        print(f"{term_encoded}: {doc_list_encoded}")
