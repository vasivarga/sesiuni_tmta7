from saptamana6POM.pages.driver import Driver


class BasePage(Driver):

    def is_element_absent(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0


