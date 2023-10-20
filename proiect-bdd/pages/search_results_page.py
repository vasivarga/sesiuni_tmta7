from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    DIV_PRODUCT_ITEM = (By.CLASS_NAME, "product-item")

    def is_products_list_size_at_least(self, size):
        return len(self.find_all(self.DIV_PRODUCT_ITEM)) >= int(size)