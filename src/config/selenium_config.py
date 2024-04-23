from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from src.config.test_data import TestData


class SeleniumConfig:

    @staticmethod
    def config_selenium() -> WebDriver:
        options = webdriver.ChromeOptions()
        options.set_capability("pageLoadStrategy", "eager")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.set_page_load_timeout(TestData.seleniumTimeout)
        driver.implicitly_wait(TestData.seleniumTimeout)

        return driver

    @staticmethod
    def close_driver(driver: WebDriver):
        if driver is not None:
            driver.close()
            driver.quit()
