import allure
import pytest


@allure.parent_suite("UI Tests")
@pytest.mark.usefixtures("before_and_after_ui_test")
class TestBaseUi:
    pass
