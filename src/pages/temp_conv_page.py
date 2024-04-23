# Temperature Conversion page
import allure
from selenium.webdriver.common.by import By

from src.pages.conversion_page import ConversionPage


class TempConvPage(ConversionPage):
    PATH = "/temperature-conversion.htm"

    # region locators
    PAGE_HDR = (By.XPATH, "//h1[text()='Temperature conversion']")

    # endregion

    @allure.step("Open Temperature Conversion page")
    def open(self):
        self.navigate(self.PATH)
        self.should_be_visible(self.PAGE_HDR)
        return self
