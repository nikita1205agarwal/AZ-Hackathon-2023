# AZ-Hackathon-2023

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

# Getting Started

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

#### Customization
-You can modify the code to scrape different sections or specific problem sets by adjusting the page_URL variable.
-The script creates a Qdatalc folder to store the scraped data. You can change the folder name or customize the folder structure by modifying the code in the script.


Feel free to contribute to the project by submitting pull requests or reporting issues.

Happy coding!

