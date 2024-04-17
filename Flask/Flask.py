from flask import Flask, request, jsonify
import pickle
import numpy as np
# must add content-type application/json to the key-value pair


app = Flask(__name__)

# Load the inverted index and similarity matrix
with open('inverted_index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)
with open('similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400

    query = data['query']
    k = data.get('k', 10)  

    # Validate the query
    if not isinstance(query, str) or not query.strip():
        return jsonify({'error': 'Invalid query'}), 400
    if not isinstance(k, int) or k < 1:
        return jsonify({'error': 'Invalid k'}), 400

    # Process the query
    query_vector = np.array([inverted_index.get(word, [0]*len(similarity_matrix)) for word in query.split()]).mean(axis=0)

    # Calculate cosine similarity
    similarities = np.dot(similarity_matrix, query_vector)

    # Get the top-K results
    top_k_indices = similarities.argsort()[-k:]
    top_k_similarities = similarities[top_k_indices]

    # Prepare the response
    response = {
        'query': query,
        'results': [{'document': int(i), 'similarity': float(s)} for i, s in zip(top_k_indices, top_k_similarities)]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, load_dotenv=False)
