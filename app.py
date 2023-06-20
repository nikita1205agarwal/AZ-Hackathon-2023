from flask import Flask, render_template, request, redirect
from lc_tfidf import load_data, calculate_sorted_order_of_documents

app = Flask(__name__)

# Load the data using the tf-idf module
vocab, documents, inverted_index = load_data()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query_string = request.form['keywords']
    query_terms = [term.lower() for term in query_string.strip().split()]
    sorted_documents = calculate_sorted_order_of_documents(query_terms)

    results = []
    for doc_index, doc in enumerate(sorted_documents):
        results.append({'heading': doc[1], 'url': doc[2], 'index': doc_index})

    return render_template('results.html', documents=results)


@app.route('/problem/<int:problem_id>')
def problem(problem_id):
    if 0 <= problem_id < len(documents):
        url = documents[problem_id][1]
        return redirect(url)
    else:
        return "Invalid problem ID"
        
# Ignore request for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)
