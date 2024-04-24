# Gloat Interview Task

## Overview

This framework is designed for UI and API testing. It utilizes the following tools:

- Pytest -> test framework
- Selenium -> UI testing
- Requests -> library for API testing
- Pydantic -> json<->model serialization/deserialization
- Allure -> detailed test reports

## Design

### Hierarchy

This is the project hierarchy with details about each part of it:

```text
project/
│
├── src/                        # Source code files
│   ├── api/                    # Functions for calling APIs
│   ├── config/                 # Configuration files
│   │   ├── selenium_config.py  # Configuration settings for Selenium
│   │   └── test_data.py        # Functions for loading test data from json file based on set env
│   ├── enums/                  # Enumerations
│   ├── exceptions/             # Custom exceptions
│   ├── models/                 # Data models for API
│   ├── pages/                  # Page object models for UI tests
│   │   └── base_page.py        # Base page object model, contans common elements, functions and driver 
│   └── utils/                  # Utility functions and helpers
│       └── rest_api_utils.py   # Utility functions for making REST API requests
│
├── tests/                      # Test files
│   ├── api_tests/              # API tests
│   │   ├── test_base_api.py    # Base class for API tests, contains common setup for all API tests
│   │   └── ...                 
│   ├── ui_tests/               # UI tests
│   │   ├── test_base_ui.py     # Base class for UI tests, contains common setup for all UI tests
│   │   └── ...
│   └── conftest.py             # Pytest configuration file
│
├── allure-results/             # Allure report data
│
├── screenshots/                # Screenshots captured during UI test failures
│
├── pytest.ini                  # Pytest configuration file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

### UI Tests

UI tests follow the Page Object Model (POM), where each webpage has its own page class and every interaction with its
elements is done on the page class level. This way we get reusable and easily maintainable code.

#### Handling UI Test Failures

In case of UI test failure, the framework automatically captures screenshot, saves it to <i>screenshots</i> folder and
attaches them to the Allure report as well.

### API Tests

Similar to POM in UI tests, here every service has its own api class and every interaction with that api is done one the
api class level. This way we get reusable and easily maintainable code. To simplify the calling of API there is
RestApiUtils class which contains a method for sending requests. Also received json is deserialized to provided model
class. If the validation of status code fails, you will get the request and response details in the assert message.

### Test data

Test data <i>(apiBaseUrl, apiKey, baseUrl,...)</i> are loaded automatically before running tests.

Test data are saved in the following path split into separate json files by environment:

```
data/environment/{env}.json
```

e.g. production test data json path:

```
data/environment/prod.json
```

For more details about how to select environment when running tests check this section [Running Tests](#running-tests).

## Setup

### Installation

1. Create virtual env:

   ```bash
   python3 -m venv venv
   ```

2. Activate virtual env:

   ```bash
   source venv/bin/activate
   ```

3. Install the project and its dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

To run the tests, use the following command:

```bash
pytest --env=prod
```

#### Available Arguments

<b>--env</b> : Set the environment where you want to run tests, Default environment is prod.

### Viewing the Allure Report locally on your machine

To generate report locally on your machine you need to follow these installation instructions:
https://allurereport.org/docs/gettingstarted-installation/

After running the tests, Allure results are automatically generated and stored to allure-results folder.
To view the Allure report, follow these steps:

1. Navigate to the root directory of the project in the terminal.
2. Run the following command to generate the Allure report:
    ```bash
    allure serve allure-results
    ```
3. The report should be automatically opened in browser.

