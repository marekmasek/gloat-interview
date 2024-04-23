import re
from typing import Union

import allure
from selenium.webdriver.common.by import By

from enums.conversions import Temperature, Length, Weight
from pages.base_page import BasePage


class ConversionPage(BasePage):
    # region locators
    UNIT_FROM_SEL = (By.ID, "unitFrom")
    UNIT_TO_SEL = (By.ID, "unitTo")
    VALUE_TO_CONVERT_INP = (By.XPATH, "//input[@id='arg' or @id='argumentConv']")
    RESULT_TXT = (By.XPATH, "//p[@id='answer' or @id='answerDisplay']")

    # endregion

    @allure.step("Select conversion units: {unit_from} to {unit_to}")
    def select_conversion_units(self, unit_from: Union[Temperature, Length, Weight],
                                unit_to: Union[Temperature, Length, Weight]):
        self.select_option(self.UNIT_FROM_SEL, str(unit_from.value))
        self.select_option(self.UNIT_TO_SEL, str(unit_to.value))

    @allure.step("Set value to convert: {value}")
    def set_value_to_convert(self, value: float):
        self.set_text(self.VALUE_TO_CONVERT_INP, str(value))

    @allure.step("Verify result: expected value = {expected_value}")
    def verify_result(self, expected_value: float):
        result_text = self.get_text(self.RESULT_TXT)
        match = re.search(r'= ([\d.]+)', result_text)
        if not match:
            raise ValueError("Can't extract the converted value from result, result value: " + result_text)
        actual_value = float(match.group(1))
        assert actual_value == expected_value, "Actual converted result value is not as expected."
