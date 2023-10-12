import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestJsAlerts(unittest.TestCase):
    alert_button = (By.CSS_SELECTOR, 'button[onclick="jsAlert()"]')
    confirm_button = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]')
    prompt_button = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]')
    result_message = (By.ID, 'result')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.find_element(*self.alert_button).click()
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(*self.result_message).text == 'You successfully clicked an alert'

    def test_accept_confirm(self):
        self.driver.find_element(*self.confirm_button).click()
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(*self.result_message).text == 'You clicked: Ok'

    def test_dismiss_confirm_alert(self):
        self.driver.find_element(*self.confirm_button).click()
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(*self.result_message).text == 'You clicked: Cancel'

    def test_accept_prompt(self):
        input_text = 'emotie'
        self.driver.find_element(*self.prompt_button).click()
        self.driver.switch_to.alert.send_keys(input_text)
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(*self.result_message).text == f'You entered: {input_text}'

    def test_dismiss_prompt(self):
        self.driver.find_element(*self.prompt_button).click()
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(*self.result_message).text == 'You entered: null'


