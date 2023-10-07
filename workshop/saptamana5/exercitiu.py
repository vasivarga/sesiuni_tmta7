import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

LINK = "https://demo.nopcommerce.com/"

driver.get(LINK)
time.sleep(1)
driver.maximize_window()

driver.find_element(By.ID, "small-searchterms").send_keys("Laptop")
driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
time.sleep(2)

lista_produse_gasite = driver.find_elements(By.CSS_SELECTOR, "div.item-box")
assert len(lista_produse_gasite) >= 2, "Eroare, nu s-a gasit numarul de rezultate dorit"

lista_preturi_elemente = driver.find_elements(By.CSS_SELECTOR, "span.actual-price")

lista_preturi_text = []

for i in range(len(lista_preturi_elemente)):
    lista_preturi_text.append(lista_preturi_elemente[i].text)

lista_preturi_text.sort()
print(lista_preturi_text[0])

expected_title = "nopCommerce demo store. Search"
actual_title = driver.title

assert expected_title == actual_title, "Eroare, titlu incorect"

