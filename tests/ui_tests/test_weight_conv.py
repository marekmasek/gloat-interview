import allure

from src.enums.conversions import Weight
from src.pages.weight_conv_page import WeightConvPage
from tests.ui_tests.test_base_ui import TestBaseUi


@allure.suite("Conversion")
@allure.sub_suite("Weight Conversion")
class TestWeightConv(TestBaseUi):

    @allure.title("Test Ounces to Grams Conversion")
    def test_ounces_to_grams_conv(self):
        weight_conv_page = WeightConvPage().open()
        weight_conv_page.accept_cookies_recommendation()
        weight_conv_page.select_conversion_units(Weight.OUNCES, Weight.GRAMS)
        weight_conv_page.set_value_to_convert(23)
        weight_conv_page.verify_result(652.039)
