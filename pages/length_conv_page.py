# Length Conversion page

import allure
from selenium.webdriver.common.by import By

from pages.conversion_page import ConversionPage


class LengthConvPage(ConversionPage):
    PATH = "/length-conversion.htm"

    # region locators
    PAGE_HDR = (By.XPATH, "//h1[text()='Length conversion']")

    # endregion

    @allure.step("Open Length Conversion page")
    def open(self):
        self.navigate(self.PATH)
        self.should_be_visible(self.PAGE_HDR)
        return self
