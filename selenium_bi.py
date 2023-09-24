from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#driver path
path = r"C:\Users\ayush\Downloads\chromedriver.exe"
chrome_service = Service(executable_path=path)
driver = webdriver.Chrome(service=chrome_service)
#driver = webdriver.Chrome(path)


#accessing url
driver.get("https://en.wikipedia.org/wiki/India")
driver.quit()