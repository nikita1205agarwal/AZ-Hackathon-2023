# AZ-Hackathon-2023

## Project Summary
This project aims to develop an intelligent search engine that allows users to search for coding problems from platforms like LeetCode, CodeChef, and Codeforces. Users can input keywords and receive a list of relevant coding problems that match their search criteria. The search engine provides problem details such as title, difficulty level, and a link to the original problem. It also allows users to filter search results based on difficulty level and programming language. The search engine utilizes the TF-IDF algorithm to ensure the relevance and accuracy of the returned problems. However, it currently excludes Algozenith's questions from the search results, although they might be integrated in the future.

# LeetCode Scraper

This Python script allows you to scrape problem links and their data from LeetCode using Selenium and Chrome WebDriver.

## Prerequisites

        Before running the script, make sure you have the following installed:

        - Python 3
        - Anaconda
        - Selenium
        - Chrome WebDriver

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
7. The script will scrape the problem links from the specified LeetCode page, clean the links, and store them in a text file named lc_problems.txt. It will also create a Qdatalc folder to store the scraped data.

## Customization

-You can modify the code to scrape different sections or specific problem sets by adjusting the page_URL variable.
-The script creates a Qdatalc folder to store the scraped data. You can change the folder name or customize the folder structure by modifying the code in the script.

## Problem Scrapping

This project not only provides access to coding problems from LeetCode but also includes scrapping problems from CodeChef and Codeforces. The scrapping functionality allows users to access a diverse range of coding challenges from these platforms.

### CodeChef

The search engine retrieves coding problems from CodeChef by leveraging its API. It fetches problem details such as problem title, difficulty level, and additional metadata. Users can search for CodeChef problems using relevant keywords and receive a list of suitable matches.

### Codeforces

Similarly, the search engine retrieves coding problems from Codeforces by utilizing its API. It fetches problem details such as problem title, difficulty level, and other relevant information. Users can search for Codeforces problems based on specific criteria and get a curated list of appropriate challenges.

Please note that the search engine integrates the problems from LeetCode, CodeChef, and Codeforces to provide users with a comprehensive collection of coding challenges to explore.

## Future Enhancements

This project is an ongoing effort, and there are plans to implement additional features and improvements in the future. Some of the upcoming enhancements include:

- Adding support for other popular coding platforms like Codeforces and CodeChef.
- Enhancing the search algorithm to provide more accurate and relevant search results.

Please note that these are just some of the planned enhancements, and the project will continue to evolve to meet the needs of the users and the developer community.

Feel free to contribute to the project by submitting pull requests or reporting issues.

Happy coding!

