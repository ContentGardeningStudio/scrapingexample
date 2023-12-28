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

projects_infos = []
for url in projects_urls:
    browser.get(url)
    dict_projects_infos = {}
    url_externe = browser.find_element(By.CLASS_NAME, 'text-bold').get_attribute('href')
    try:
        tag = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[1]/div[3]/a[2]/strong"))
        )
        dict_projects_infos['tags'] = tag.text

        star = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[7]/a/strong'))
        )
        dict_projects_infos['stars'] = star.text

        fork = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[9]/a/strong'))
        )
        dict_projects_infos['forks'] = fork.text

        commit = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/ul/li/a/span/strong'))
        )
        dict_projects_infos['commits'] = commit.text
        projects_infos.append(dict_projects_infos)

        # projects_infos = list(set(projects_infos))
        # is_same = False
        # res_list = []
        # for i in range(len(projects_infos)):
        #     if projects_infos[i] not in projects_infos[i + 1:]:
        #         res_list.append(projects_infos[i])
        # print(res_list)

        # res_list = {frozenset(item.items()):
        #                 item for item in projects_infos}.values()
        # print(res_list)
        # res_list = projects_infos[-1]

        # affichage des infos des 2 premiers projets
        print(projects_infos)

    finally:
        pass
    #languages = browser.find_elements(By.CLASS_NAME, 'color-fg-default text-bold mr-1')
    #description = browser.find_elements(By.CLASS_NAME, 'BorderGrid about-margin')
    #time.sleep(10)
    # try except faire a la fin