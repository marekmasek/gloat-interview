# Gloat Interview Task

## Overview

todo

## Hierarchy

```
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
│   │   └── base_page.py        # Base page object model, contans common elements, functions and an instance of driver is stored here 
│   ├── utils/                  # Utility functions and helpers
│   │   └── rest_api_utils.py   # Utility functions for making REST API requests
│   └── ...
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

## Installation

To install the project and its dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Running Tests

To run the tests, use the following command:

```bash
pip pytest --env=prod
```
