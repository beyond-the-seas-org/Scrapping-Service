from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

#chrome_options = Options()
    # disabling the pop up of browser window
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome()

try:
    driver.get("https://ieeexplore.ieee.org/document/10204393/keywords?fbclid=IwAR1WGJabY5_WmcCIR35CIbeeq-SEXf5nPPMeGQ4ly8Fk9fiSv71nsjh-HzY#keywords")


    keywords = driver.find_elements(By.CLASS_NAME, 'u-p-0')
    print(keywords)


except Exception as e:
    print(e)
