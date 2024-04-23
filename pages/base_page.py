import threading
from typing import Tuple

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config.selenium_config import SeleniumConfig
from config.test_data import TestData
from exceptions.exceptions import ElementShould
from utils.url_utils import UrlUtils


class BasePage:
    # region base locators
    CONTINUE_WITH_RECOMMENDED_COOKIES_BTN = (By.ID, "ez-accept-all")

    # endregion

    @allure.step("Accept cookies recommendation")
    def accept_cookies_recommendation(self):
        self.click(self.CONTINUE_WITH_RECOMMENDED_COOKIES_BTN)

    # region driver management

    _driver_storage = threading.local()

    @staticmethod
    def get_driver():
        if not hasattr(BasePage._driver_storage, 'driver'):
            BasePage._driver_storage.driver = SeleniumConfig.config_selenium()
        return BasePage._driver_storage.driver

    @staticmethod
    def get_wait():
        if not hasattr(BasePage._driver_storage, 'wait'):
            BasePage._driver_storage.wait = WebDriverWait(BasePage.get_driver(), TestData.seleniumTimeout)
        return BasePage._driver_storage.wait

    @staticmethod
    def quit_driver():
        if hasattr(BasePage._driver_storage, 'driver'):
            SeleniumConfig.close_driver(BasePage.get_driver())
            del BasePage._driver_storage.driver
        if hasattr(BasePage._driver_storage, 'wait'):
            del BasePage._driver_storage.wait

    # endregion

    # region selenium wrapper functions
    def highlight(self, element):
        self.get_driver().execute_script(
            "arguments[0].setAttribute('style', 'border: 3px solid red; border-style: dashed;');", element)

    def click(self, locator: Tuple[str, str]):
        el = self.should_be_clickable(locator)
        self.highlight(el)
        el.click()

    def set_text(self, locator: Tuple[str, str], txt: str):
        el = self.should_be_clickable(locator)
        el.clear()
        self.highlight(el)
        el.send_keys(txt)

    def get_text(self, locator: Tuple[str, str]) -> str:
        el = self.should_be_visible(locator)
        self.highlight(el)
        return el.text

    def select_option(self, locator: Tuple[str, str], txt: str):
        el = self.should_be_clickable(locator)
        self.highlight(el)
        Select(el).select_by_visible_text(txt)

    def should_be_visible(self, locator: Tuple[str, str]) -> WebElement:
        try:
            return self.get_wait().until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            raise ElementShould(
                f"Element should be visible, but it's not.\nElement: {locator}\nTimeout: {TestData.seleniumTimeout}s")

    def should_be_clickable(self, locator: Tuple[str, str]) -> WebElement:
        try:
            return self.get_wait().until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            raise ElementShould(
                f"Element should be clickable, but it's not.\nElement: {locator}\nTimeout: {TestData.seleniumTimeout}s")

    def navigate(self, path_or_url: str):
        """
        Loads a web page in the current browser session.
        :param path_or_url: Either the complete URL of the web page
                            or a relative path that will be combined with the base URL.
        """
        self.get_driver().get(UrlUtils.get_complete_url(TestData.baseUrl, path_or_url))
    # endregion
