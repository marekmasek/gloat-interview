# Weight Conversion page

import allure
from selenium.webdriver.common.by import By

from src.pages.conversion_page import ConversionPage


class WeightConvPage(ConversionPage):
    PATH = "/weight-conversion.htm"

    # region locators
    PAGE_HDR = (By.XPATH, "//h1[text()='Weight conversion']")

    # endregion

    @allure.step("Open Weight Conversion page")
    def open(self):
        self.navigate(self.PATH)
        self.should_be_visible(self.PAGE_HDR)
        return self
