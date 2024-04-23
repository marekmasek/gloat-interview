from datetime import datetime
from pathlib import Path

import allure
import pytest

from src.config.test_data import TestData
from src.pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod")
    # todo add another one for browser selection...


def pytest_configure(config):
    env = config.getoption('env')
    TestData.load_test_data(env)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # Check if it's failed test and was run with before_and_after_ui_test fixture, to be sure it's UI test
    if rep.when == 'call' and rep.failed:
        contains_mark = any(
            mark.name == 'usefixtures' and 'before_and_after_ui_test' in mark.args
            for mark in item.own_markers + item.parent.own_markers
        )
        if contains_mark:
            # create screenshots folder, take a screenshot and save it
            path = Path(__file__).absolute().parent.parent / "screenshots"
            path.mkdir(parents=True, exist_ok=True)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            path = path / f"{item.name}-{now}.png"
            screenshot = BasePage.get_driver().get_screenshot_as_png()
            with open(path, "wb") as file:
                file.write(screenshot)
            # attach the screenshot to allure report
            allure.attach(
                screenshot,
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="function", autouse=True)
def before_and_after_ui_test():
    # add before test here
    yield
    BasePage.quit_driver()
