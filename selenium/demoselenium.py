import csv
import time

import selenium.common.exceptions
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
# Open the website
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get("https://github.com/collections/machine-learning")

# Extract all projects
projects = browser.find_elements(By.TAG_NAME, 'h1')[1:]
projects_urls = []
for project in projects:
    try:
        proj_url = project.find_element(By.TAG_NAME, 'a').get_attribute('href')
        projects_urls.append(proj_url)
    except selenium.common.exceptions.NoSuchElementException:
        pass


for url in projects_urls:
    browser.get(url)
    url_externe = browser.find_element(By.CLASS_NAME, 'text-bold').get_attribute('href')
    try:
        tag = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[1]/div[3]/a[2]/strong"))
        )
        star = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[7]/a/strong'))
        )
        fork = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[9]/a/strong'))
        )
        fork = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[9]/a/strong'))
        )
        commit = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/ul/li/a/span/strong'))
        )
        print(url_externe)
        print(tag.text + ' tags')
        print(star.text + ' stars')
        print(fork.text + ' forks')
        print(commit.text + ' commits')
        print('---------')
    finally:
        pass
    #languages = browser.find_elements(By.CLASS_NAME, 'color-fg-default text-bold mr-1')
    #description = browser.find_elements(By.CLASS_NAME, 'BorderGrid about-margin')
    #time.sleep(10)
    # try except faire a la fin