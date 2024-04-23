import allure

from src.enums.conversions import Temperature
from src.pages.temp_conv_page import TempConvPage
from tests.ui_tests.test_base_ui import TestBaseUi


@allure.suite("Conversion")
@allure.sub_suite("Temperature Conversion")
class TestTempConv(TestBaseUi):

    @allure.title("Test Celsius to Fahrenheit Conversion")
    def test_celsius_to_fahrenheit_conv(self):
        temp_conv_page = TempConvPage().open()
        temp_conv_page.accept_cookies_recommendation()
        temp_conv_page.select_conversion_units(Temperature.CELSIUS, Temperature.FAHRENHEIT)
        temp_conv_page.set_value_to_convert(20)
        temp_conv_page.verify_result(68)
