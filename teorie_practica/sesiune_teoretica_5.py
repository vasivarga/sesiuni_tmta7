import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiem un obiect al clasei Chrome din libraria webdriver
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.ID, "first-name").send_keys("Popescu")
chrome.find_element(By.CLASS_NAME, "form-control").send_keys("Popescu")
time.sleep(3)
chrome.find_element(By.LINK_TEXT, "Submit").click()
# chrome.find_element(By.PARTIAL_LINK_TEXT, "Sub").click()
time.sleep(3) # "adoarme" procesul timp de 3 secunde