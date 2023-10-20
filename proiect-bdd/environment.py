from browser import Browser
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.search_results_page = SearchResultsPage()
    context.home_page = HomePage()
    context.register_page = RegisterPage()


def after_all(context):
    context.browser.close()
