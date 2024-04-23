import allure

from src.enums.conversions import Length
from src.pages.length_conv_page import LengthConvPage
from tests.ui_tests.test_base_ui import TestBaseUi


@allure.suite("Conversion")
@allure.sub_suite("Length Conversion")
class TestLengthConv(TestBaseUi):

    @allure.title("Test Meters to Feet Conversion")
    def test_meters_to_feet_conv(self):
        length_conv_page = LengthConvPage().open()
        length_conv_page.accept_cookies_recommendation()
        length_conv_page.select_conversion_units(Length.METERS, Length.FEET)
        length_conv_page.set_value_to_convert(12)
        length_conv_page.verify_result(39.37)
