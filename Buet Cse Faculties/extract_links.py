from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json


def extract_links():
    base = "https://cse.buet.ac.bd/faculty_list"
    driver = webdriver.Chrome()



    file = open("buet-cse-faculty-list-links.txt", "w", encoding="utf-8")

    #store the links in a set first to avoid duplicates
    links = set()
    data = {}
    link = base
    print(link)

    driver.get(link)
    time.sleep(5)
    link_contents = driver.find_elements(By.CLASS_NAME, 'row')
    print(link_contents)

    for contents in link_contents:
        contents = contents.find_elements(By.TAG_NAME, 'a')
        for content in contents:
            url = content.get_attribute('href')
            #if url does not starts with https://cse.buet.ac.bd/faculty_list/detail/ then skip
            if not url.startswith("https://cse.buet.ac.bd/faculty_list/detail/"):
                continue
            name = content.text
            #remove the numeric value from the name, that is skip index 0
            name = name.split(" ", 1)[1]
            links.add(content.get_attribute('href'))
            data[name] = url

    driver.close()
    json.dump(data, file, indent=4, ensure_ascii=False)
    file.flush()


extract_links()
            



