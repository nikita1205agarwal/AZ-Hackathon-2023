# AZ-Hackathon-2023

## Project Summary
This project aims to develop an intelligent search engine that allows users to search for coding problems from Leetcode. Users can input keywords and receive a list of relevant coding problems that match their search criteria. The search engine provides problem details such as title, difficulty level, and a link to the original problem. It also allows users to filter search results based on difficulty level and programming language. The search engine utilizes the TF-IDF algorithm to ensure the relevance and accuracy of the returned problems.

# LeetCode Scraper

This Python script allows you to scrape problem links and their data from LeetCode using Selenium and Chrome WebDriver.

## Prerequisites

        Before running the script, make sure you have the following installed:

        - Python 3
        - Anaconda
        - Selenium
        - Chrome WebDriver
        - NLTK library

        You can install Selenium and Chrome WebDriver using pip:

        ```shell
        pip install selenium
        pip install webdriver_manager
        
## Getting Started

1. Clone the repository to your local machine: 
        git clone https://github.com/your-username/leetcode-scraper.git
2. Navigate to the project directory:
        cd leetcode-scraper
3. Create a virtual environment (optional but recommended):
        conda create --name leetcode-scraper-env python=3.9
        conda activate leetcode-scraper-env
4. Install the required packages:
        pip install -r requirements.txt
5. Update the page_URL variable in the script to specify the LeetCode problem set URL you want to scrape.
6. Run the script:
        python leetcode_scraper.py
7. The script will scrape the problem links from the specified LeetCode page, clean the links, and store them in a text file named lc_problems.txt. It will also create a Qdatalc folder to store the scraped data. Inside the qdatalc folder, you will find a data folder that contains the scraped questions files, indexlc.txt, and qindexlc.txt.

## TF-IDF Implementation
The project also includes an implementation of the TF-IDF algorithm for text analysis. This algorithm calculates the relevance scores of documents based on the frequency of terms in each document and their inverse document frequency across the entire collection.

### Data Pre-processing
Before applying TF-IDF, the data undergoes pre-processing steps, including the removal of stopwords and leading numbers from the text.

### Loading and Processing Data
The load_data() function reads the input file, pre-processes the data, builds the vocabulary, and constructs the inverted index. It utilizes the NLTK library to tokenize the text and remove stopwords.

### Vocabulary and Inverted Index
The vocabulary is a collection of unique terms present in the documents, along with their corresponding IDF (Inverse Document Frequency) values. The inverted index maps each term to the documents in which it appears.

### Calculating Relevance Scores
The calculate_sorted_order_of_documents(query_terms) function calculates the relevance scores for a given set of query terms. It retrieves the matching documents and ranks them based on their relevance scores.

### Usage
To use the TF-IDF functionality, follow these steps:

- Make sure you have the required dependencies installed, including NLTK.
- Call the load_data() function to load and process the data.
- Use the calculate_sorted_order_of_documents(query_terms) function to perform a query and retrieve the matching documents.
        
## Customization

- You can modify the code to scrape different sections or specific problem sets by adjusting the page_URL variable in the script.
- The script creates a Qdatalc folder to store the scraped data. You can change the folder name or customize the folder structure by modifying the code in the script.
- You can customize the data cleaning process in the clean_text() function with your query terms to obtain the sorted order of documents based on relevance scores.

## Future Enhancements

Here are some planned enhancements for the project:

- Implement a user interface (UI) for the search engine to provide a more user-friendly experience.
- Add support for additional coding problem platforms, such as HackerRank and Codeforces, to expand the search capabilities.
- Improve the efficiency of the TF-IDF algorithm by optimizing the data structures and algorithms used in the inverted index construction and query processing.

Please note that these are just some of the planned enhancements, and the project will continue to evolve to meet the needs of the users and the developer community.

Feel free to contribute to the project by submitting pull requests or reporting issues.

Happy coding!
