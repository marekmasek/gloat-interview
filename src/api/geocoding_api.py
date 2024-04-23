import allure

from src.models.location_by_zip_response import LocationByZipResponse
from src.utils.rest_api_utils import RestApiUtils, HttpMethod


class GeocodingApi:
    BASE_PATH = "/geo/1.0"

    @allure.step("Calling Geocoding API to get coordinates for zip code")
    def get_coordinates_by_zip(self, zip_code: str, country_code: str) -> LocationByZipResponse:
        return RestApiUtils.send_request(HttpMethod.GET,
                                         self.BASE_PATH + "/zip",
                                         LocationByZipResponse,
                                         params={"zip": zip_code + "," + country_code},
                                         expected_status_code=200
                                         )
