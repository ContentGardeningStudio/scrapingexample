import csv
import time

import selenium.common.exceptions
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
# Open the website
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get("https://github.com/collections/machine-learning")

# Extract all projects
projects = browser.find_elements(By.TAG_NAME, 'h1')[1:]
list_projects = []
# projects_urls = []
for project in projects:
    try:
        proj_url = project.find_element(By.TAG_NAME, 'a').get_attribute('href')
        # print(proj_url)
        #proj_url.click()
        list_projects.append(proj_url)
        # print(browser)
        # browser.find_element(By.CLASS_NAME, 'ml-3 Link--primary no-underline').click()
    except selenium.common.exceptions.NoSuchElementException:
        pass


for lp in list_projects:
    browser.get(lp)
    url_externe = browser.find_element(By.CLASS_NAME, 'text-bold').get_attribute('href')
    # description = browser.find_element(By.CLASS_NAME, 'f4 my-3')
    print(url_externe)
    # print(description.text)
