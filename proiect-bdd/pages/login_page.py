from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    DIV_ERROR_MESSAGE_MAIN = (By.CLASS_NAME, "message-error")
    SPAN_ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email_text):
        # self.driver.find_element(*self.INPUT_EMAIL).send_keys(email_text)
        self.type(self.INPUT_EMAIL, email_text)

    def set_password(self, pass_text):
        self.type(self.INPUT_PASSWORD, pass_text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def is_main_error_message_displayed(self):
        return self.find(self.DIV_ERROR_MESSAGE_MAIN).is_displayed()

    def get_main_error_message_text(self):
        return self.get_text(self.DIV_ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.find(self.SPAN_ERROR_MESSAGE_EMAIL).is_displayed()

    def get_email_error_message_text(self):
        return self.get_text(self.SPAN_ERROR_MESSAGE_EMAIL)









