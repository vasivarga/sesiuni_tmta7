import time
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest(unittest.TestCase):
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.TAG_NAME, 'button')
    banner = (By.ID, 'flash')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_valid_login(self):
        self.driver.find_element(*self.username_input).send_keys('tomsmith')
        self.driver.find_element(*self.password_input).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.login_button).click()
        self.driver.implicitly_wait(3)  # wait implicit pentru toate elementele de pe pagina respectiva
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'flash'))) # wait explicit pentru UN element
        # time.sleep(3) # wait implicit pentru toate elementele de pe pagina respectiva
        self.assertEqual(self.driver.find_element(*self.banner).text, 'You logged into a secure area!\n×')

    @unittest.skip
    def test_invalid_login(self):
        self.driver.find_element(*self.username_input).send_keys('tomsmith')
        self.driver.find_element(*self.password_input).send_keys('126543')
        self.driver.find_element(*self.login_button).click()
        self.assertEqual(self.driver.find_element(*self.banner).text, 'Your password is invalid!\n×')
