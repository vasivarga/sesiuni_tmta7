import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# varianta pentru Firefox:
# from webdriver_manager.firefox import GeckoDriverManager


class LoginPageTest(unittest.TestCase):
    MAIN_URL = "https://www.saucedemo.com/"
    TEXT_STANDARD_USER = "standard_user"
    TEXT_PASSWORD = "secret_sauce"
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    H3_LOGIN_ERROR = (By.XPATH, "//h3[@data-test='error']")  # h3[data-test='error']


    def setUp(self) -> None:
        # pentru Firefox avem GeckoDriverManager()
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.MAIN_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_page_title(self):
        expected_title = "Swag Labs"
        actual_title = self.driver.title

        # assert expected_title == actual_title, "Unexpected title"
        self.assertEquals(expected_title, actual_title, "Unexpected title")

    def test_elements_are_visible(self):
        # assert self.driver.find_element(*self.INPUT_USERNAME).is_displayed()
        self.assertTrue(self.driver.find_element(*self.INPUT_USERNAME).is_displayed(), "Username input is not visible")
        self.assertTrue(self.driver.find_element(*self.INPUT_PASSWORD).is_displayed(), "Password input is not visible")
        self.assertTrue(self.driver.find_element(*self.BUTTON_LOGIN).is_displayed(), "Login button is not visible")

    def test_valid_login(self):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(self.TEXT_STANDARD_USER)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(self.TEXT_PASSWORD)
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        # assert "inventory" in self.driver.current_url, "Login failed"
        self.assertIn("inventory", self.driver.current_url, "Login failed")

    def test_invalid_login(self):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys("username")
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys("password")
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        self.assertTrue(self.driver.find_element(*self.H3_LOGIN_ERROR).is_displayed(), "Login error not displayed")
