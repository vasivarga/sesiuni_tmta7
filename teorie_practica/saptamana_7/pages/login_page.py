from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.TAG_NAME, 'button')
    banner = (By.ID, 'flash')

    def send_valid_username(self):
        self.driver.find_element(*self.username_input).send_keys('tomsmith')

    def send_valid_password(self):
        self.driver.find_element(*self.password_input).send_keys('SuperSecretPassword!')

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def check_success_message(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, 'flash')))
        assert self.driver.find_element(*self.banner).text, "You logged into a secure area!\n×"

    def send_invalid_username_or_password(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def check_error_message(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, 'flash')))
        assert self.driver.find_element(*self.banner).text, 'Your password is invalid!\n×'
