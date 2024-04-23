import logging
from enum import Enum, auto
from typing import Type, TypeVar

import requests
from pydantic import BaseModel

from src.config.test_data import TestData
from src.utils.url_utils import UrlUtils


class HttpMethod(Enum):
    DELETE = auto()
    GET = auto()
    HEAD = auto()
    OPTIONS = auto()
    PATCH = auto()
    POST = auto()
    PUT = auto()


class RestApiUtils:
    T = TypeVar('T', bound=BaseModel)

    @staticmethod
    def send_request(method: HttpMethod, path_or_url: str, model: Type[BaseModel], headers: dict = None,
                     params: dict = None, payload: BaseModel = None, app_id: str = TestData.apiKey,
                     expected_status_code: int = None) -> T:
        """
        Sends an HTTP request and returns the response mapped to the provided Pydantic model.

        Args:
            method: The HTTP method to use for the request.
            path_or_url: The URL or path of the API endpoint. If path is provided, it will use base api url + path.
            model: The Pydantic model used for validating the response JSON.
            headers: Optional headers to include in the request.
            params: Optional query parameters to include in the request.
            payload: Optional Pydantic model instance to be converted to JSON and sent as the request body.
            app_id: API key, if argument is not sent, the default one is used, if you want to send it without API key,
                    set it to None
            expected_status_code: The expected HTTP status code of the response.

        Returns:
            The response mapped to the provided Pydantic model.

        Raises:
            AssertionError: If the actual status code does not match the expected status code.
        """

        # setting up appid if it's not set to None
        if app_id is not None:
            if params is None:
                params = {}
            params["appid"] = app_id

        url = UrlUtils.get_complete_url(TestData.apiBaseUrl, path_or_url)
        json_payload = payload.json() if payload is not None else None

        # making request
        res = requests.request(method.name, url, headers=headers, params=params, json=json_payload)
        logging.debug(
            f"\n\nREQUEST:\nmethod: {method.name}\nurl: {url}\nparams: {params}\nheaders: {headers}" +
            f"\nbody: {json_payload}" +
            f"\n\nRESPONSE:\nstatus code:{res.status_code}\nheaders: {res.headers}\nbody: {res.text}\n")

        # checking expected status code
        if expected_status_code is not None:
            assert res.status_code == expected_status_code, \
                f"Expected status code {expected_status_code}, but got {res.status_code}"

        # returning response mapped to the provided model
        return model.model_validate(res.json())
