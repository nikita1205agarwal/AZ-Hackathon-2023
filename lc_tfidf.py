import chardet
import os
import math
from pathlib import Path
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Detect the encoding of a file
def find_encoding(fname):
    with open(fname, 'rb') as f:
        r_file = f.read()
        result = chardet.detect(r_file)
        charenc = result['encoding']
    return charenc

# Data pre-processing: stopwords removal and removal of any leading numbers from the string
def preprocess(document_text):
    stopwords_set = set(stopwords.words('english'))
    terms = [term.lower() for term in document_text.strip().split()[1:] if term.lower() not in stopwords_set]
    return terms

# Read the input file, preprocess the data, build the vocabulary, and construct the inverted index.
def load_data():
    vocab = Counter()
    documents = []
    inverted_index = {}

    directory = Path('Qdatalc/')
    file_names = [
        directory / 'indexlc.txt',
        directory / 'Qindexlc.txt',
    ]

    data_directory = directory / 'data'
    file_names.extend(data_directory.rglob('*'))

    for filename in file_names:
        my_encoding = find_encoding(filename)

        with open(filename, 'r', encoding=my_encoding) as f:
            lines = f.readlines()

        for index, line in enumerate(lines):
            tokens = preprocess(line)
            documents.append(tokens)
            for token in tokens:
                vocab[token] += 1
                inverted_index.setdefault(token, []).append(index)

    vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))
    save_data(vocab, documents, inverted_index)

# Save the vocabulary, IDF values, documents, and inverted index into separate text files
def save_data(vocab, documents, inverted_index):
    output_dir = Path('tf-idf_lc')
    output_dir.mkdir(exist_ok=True)

    # Save the vocab in a text file
    with open(output_dir / 'vocab_lc.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(vocab.keys()))

    # Save the idf values in a text file
    with open(output_dir / 'idf-values_lc.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(str(vocab[key]) for key in vocab.keys()))

    # Save the documents in a text file
    with open(output_dir / 'documents_lc.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(' '.join(document) for document in documents))

    # Save the inverted index in a text file
    with open(output_dir / 'inverted-index_lc.txt', 'w', encoding='utf-8') as f:
        for key, value in inverted_index.items():
            f.write(f"{key}\n")
            f.write(' '.join(str(doc_id) for doc_id in value))
            f.write('\n')

# Load the vocabulary and IDF values from the text files
def load_vocab():
    vocab = {}
    with open('tf-idf_lc/vocab_lc.txt', 'r', encoding='utf-8') as f:
        vocab_terms = f.readlines()
    with open('tf-idf_lc/idf-values_lc.txt', 'r', encoding='utf-8') as f:
        idf_values = f.readlines()

    for (term, idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    return vocab

# Load the preprocessed documents from the text file
def load_documents():
    with open('tf-idf_lc/documents_lc.txt', 'r', encoding='utf-8') as f:
        documents = [document.strip().split() for document in f.readlines()]
    return documents

# Load the inverted index from a text file
def load_inverted_index():
    inverted_index = {}
    with open('tf-idf_lc/inverted-index_lc.txt', 'r', encoding='utf-8') as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0, len(inverted_index_terms), 2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num + 1].strip().split()
        inverted_index[term] = documents
    return inverted_index

# Calculate term frequency
def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1

    for document in tf_values:
        tf_values[document] /= len(documents[int(document)])

    return tf_values

# Calculate inverse document frequency
def get_idf_value(term):
    return math.log(len(documents) / vocab_idf_values[term])

# Extract heading part
def fetch_text_by_index(file_path, index):
    if index is None:
        return None  # Return None if line number is None

    with open(file_path, 'r', encoding=find_encoding(file_path)) as file:
        lines = file.readlines()
        line = lines[index]
        parts = line.strip().split('.', 1)
        return parts[1].strip()

# Extract URL of the corresponding heading
def fetch_data_by_line(file_path, line_number):
    with open(file_path, 'r', encoding=find_encoding(file_path)) as file:
        lines = file.readlines()
        return lines[line_number].strip()

# Calculate the relevance scores for the given query terms and retrieve the matching documents
def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    for term in query_terms:
        if term in vocab_idf_values and vocab_idf_values[term] != 0:
            tf_values_by_document = get_tf_dictionary(term)
            idf_value = get_idf_value(term)
            for document in tf_values_by_document:
                if document not in potential_documents:
                    potential_documents[document] = tf_values_by_document[document] * idf_value
                potential_documents[document] += tf_values_by_document[document] * idf_value

    if not potential_documents:
        return []
    else:
        for document in potential_documents:
            potential_documents[document] /= len(query_terms)

        potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

        sorted_documents = []

        heading = 'Qdatalc/indexlc.txt'
        link = 'Qdatalc/Qindexlc.txt'
       
        for doc_index in potential_documents:
            index=int(doc_index)-1
            heading_text = fetch_text_by_index(heading, index)
            if heading_text is None:
                continue
            url_text = fetch_data_by_line(link, index)
            sorted_documents.append((doc_index, heading_text, url_text))

        return sorted_documents

# Load the data if not already loaded
def load_and_process_data():
    if not os.path.exists('tf-idf_lc/vocab_lc.txt') or not os.path.exists('tf-idf_lc/idf-values_lc.txt') or not os.path.exists(
            'tf-idf_lc/documents_lc.txt') or not os.path.exists('tf-idf_lc/inverted-index_lc.txt'):
        load_data()
    vocab_idf_values = load_vocab()
    documents = load_documents()
    inverted_index = load_inverted_index()
    return vocab_idf_values, documents, inverted_index

vocab_idf_values, documents, inverted_index = load_and_process_data()
