from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

dictt = {}
dict = {"name": "University of California, San Diego", "rank": "1", "location": "Location not found"}

print(dict.keys().__contains__("error"))