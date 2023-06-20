#importing required modules
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Setting up the web driver
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Function to get all the 'a' tags from a given URL
def get_a_tags(url):
    driver.get(url) 
    time.sleep(10) 
    links = driver.find_elements(By.TAG_NAME, "a") 
    ans = []
    for i in links: 
        try:
            if "/problems/" in i.get_attribute("href"): 
                ans.append(i.get_attribute("href")) 
        except:
            pass
    ans = list(set(ans)) 
    return ans

# Function to remove elements with a specific pattern from an array
def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed: " + element)
    return new_array

# Function to get an array of links from a file
def get_array_of_links():
    arr = []  # Array to store the lines of the file
    # with open("lc_problems.txt", "r") as file:
    with open('lc_problems.txt', 'r', encoding='utf-8') as file:
        for line in file:
            arr.append(line.strip())
    return arr

# Function to add text to the "index.txt" file
def add_text_to_index_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "indexlc.txt")
    # with open(index_file_path, "a") as index_file:
    with open('index_file_path.txt', 'a', encoding='utf-8') as index_file:
        index_file.write(text + "\n")
        
# Function to add a link to the "Qindex.txt" file
def add_link_to_Qindex_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "Qindexlc.txt")
    with open(index_file_path, "a", encoding='utf-8') as Qindex_file:            
        Qindex_file.write(text+"\n") 
        
# Function to create and add text to a file
def create_and_add_text_to_file(file_name, text):
    folder_path = os.path.join(QDATA_FOLDER, file_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name + ".txt")
    with open(file_path, "w", encoding="utf-8", errors="ignore") as new_file:
        new_file.write(text)

# Function to scrape and process page data
def getPageData(url, index):
    heading_class = ".mr-2.text-label-1"
    body_class = ".px-5.pt-4"
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, body_class)))
        time.sleep(1)
        heading = driver.find_element(By.CSS_SELECTOR, heading_class)
        body = driver.find_element(By.CSS_SELECTOR, body_class)
        print(heading.text)
        if (heading.text):
            add_text_to_index_file(heading.text)
            add_link_to_Qindex_file(url)
            create_and_add_text_to_file(str(index), body.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False
      
# Scrape the links from LeetCode pages
page_URL = "https://leetcode.com/problemset/all/?page="
my_ans = []
for i in range(1, 56):
    my_ans += (get_a_tags(page_URL+str(i)))
my_ans = list(set(my_ans))
with open('lc.txt', 'a', encoding='utf-8') as f:
    for j in my_ans:
        f.write(j+'\n')
    
# Process the links and scrape page data:
arr = []  
with open("lc.txt", "r", encoding='utf-8') as file:
    for line in file:
        arr.append(line.strip()) 
arr = remove_elements_with_pattern(arr, "/solution")
arr = list(set(arr))
with open('lc_problems.txt', 'a', encoding='utf-8') as f:
    for j in arr:
        f.write(j+'\n')     
index = 1
QDATA_FOLDER = "Qdatalc"
os.makedirs(QDATA_FOLDER, exist_ok=True)
arr = get_array_of_links()
for link in arr:
    success = getPageData(link, index)
    if (success):
        index = index+1
driver.quit()
