import allure

from src.models.onecall_response import OneCallResponse
from src.utils.rest_api_utils import RestApiUtils, HttpMethod


class OneCallApi:
    path = "/data/3.0/onecall"

    @allure.step("Calling OneCall API to get forecast")
    def get_forecast(self, lon: float, lat: float) -> OneCallResponse:
        return RestApiUtils.send_request(HttpMethod.GET,
                                         self.path,
                                         OneCallResponse,
                                         params={"lon": lon, "lat": lat, "units": "metric"},
                                         expected_status_code=200
                                         )
