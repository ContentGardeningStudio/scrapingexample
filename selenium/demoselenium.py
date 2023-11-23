import csv
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
for project in projects:
    dict_projects = {}
    # print(project.text)
    proj_name = project.text
    dict_projects['name'] = proj_name
    # print(proj_name)
    try:
        proj_url = project.find_element(By.TAG_NAME, 'a').get_attribute('href')
        # print(proj_url)
        dict_projects['url'] = proj_url
        # print(dict_projects)
        list_projects.append(dict_projects)
    except selenium.common.exceptions.NoSuchElementException:
        pass

headers = ['name', 'url']
with open('projects.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(list_projects)

browser.quit()