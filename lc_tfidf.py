# Import required libraries
import chardet
import os
import math
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#  Detect the encoding of a file
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

# data pre-processing: stopwords removal and removal of any leading numbers from the string
def preprocess(document_text):
    stopwords_set = set(stopwords.words('english'))
    terms = [term.lower() for term in document_text.strip().split()[1:] if term.lower() not in stopwords_set]
    return terms

# read the input file, preprocess the data, build the vocabulary, and construct the inverted index.   
def load_data():
    vocab = {}
    documents = []
    inverted_index = {}

    directory = 'Qdatalc/'
    file_names = []

    file_names.append(os.path.join(directory, 'indexlc.txt'))
    file_names.append(os.path.join(directory, 'Qindexlc.txt'))

    for root, dirs, files in os.walk(os.path.join(directory, 'data')):
        for file in files:
            file_names.append(os.path.join(root, file))
    
    for filename in file_names:
        my_encoding = find_encoding(filename)

        with open(filename, 'r', encoding=my_encoding) as f:
            lines = f.readlines()
            
        for index, line in enumerate(lines):
            tokens = preprocess(line)
            documents.append(tokens)
            for token in tokens:
                vocab[token] = vocab.get(token, 0) + 1
                if token not in inverted_index:
                    inverted_index[token] = [index]
                else:
                    inverted_index[token].append(index)

    vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))
    save_data(vocab, documents, inverted_index)

    return vocab, documents, inverted_index

# Save the vocabulary, IDF values, documents, and inverted index into separate text files
def save_data(vocab, documents, inverted_index):
    # Save the vocab in a text file
    with open('tf-idf_lc/vocab_lc.txt', 'w', encoding='utf-8') as f:
        for key in vocab.keys():
            f.write("%s\n" % key)

    # Save the idf values in a text file
    with open('tf-idf_lc/idf-values_lc.txt', 'w', encoding='utf-8') as f:
        for key in vocab.keys():
            f.write("%s\n" % vocab[key])

    # Save the documents in a text file
    with open('tf-idf_lc/documents_lc.txt', 'w', encoding='utf-8') as f:
        for document in documents:
            f.write("%s\n" % ' '.join(document))
            
    # Save the inverted index in a text file
    with open('tf-idf_lc/inverted-index_lc.txt', 'w', encoding='utf-8') as f:
        for key in inverted_index.keys():
            f.write("%s\n" % key)
            f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))

vocab_idf_values, documents, inverted_index = load_data()

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
    documents = []
    with open('tf-idf_lc/documents_lc.txt', 'r', encoding='utf-8') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]

    #print('Number of documents:', len(documents))
    #print('Sample document:', documents[0])
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
    
    #print('Size of inverted index:', len(inverted_index))
    return inverted_index

vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()

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

# extract heading part
def fetch_text_by_index(file_path, index):
    if index is None:
        return None  # Return None if line number is None

    with open(file_path, 'r', encoding=find_encoding(file_path)) as file:
        lines = file.readlines()
        line = lines[index]
        parts = line.strip().split('.', 1)
        return parts[1]
    #return None  # Return None if line number is out of range

# extract url of the corresponding heading
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
        # print(potential_documents) key, score

        sorted_documents = []

        heading = 'Qdatalc/indexlc.txt'
        link = 'Qdatalc/Qindexlc.txt'
        
        for doc_index in potential_documents:
            heading_text = fetch_text_by_index(heading, doc_index)
            if heading_text is None:
                continue
            url_text = fetch_data_by_line(link, doc_index)
            sorted_documents.append((doc_index, heading_text, url_text))

        return sorted_documents
