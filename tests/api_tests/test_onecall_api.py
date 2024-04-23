from datetime import timedelta

import allure

from src.api.geocoding_api import GeocodingApi
from src.api.onecall_api import OneCallApi
from src.utils.date_time_utils import DateTimeUtils
from tests.api_tests.test_base_api import TestBaseApi


@allure.suite("OneCall API")
@allure.sub_suite("Daily Forecast")
class TestOneCallApi(TestBaseApi):

    @allure.title("Test Tomorrow's Temperature Within 10% of Today's")
    def test_tomorrows_temp_within_10_percent_of_today(self):
        # get location coordinates and forecast data
        location = GeocodingApi().get_coordinates_by_zip("20852", "US")
        forecast = OneCallApi().get_forecast(location.lon, location.lat)

        # get today's and tomorrow's dates in the location timezone offset
        tz_offset = forecast.timezone_offset
        today_date_tz = DateTimeUtils.now(tz_offset_seconds=tz_offset).date()
        tomorrow_date_tz = today_date_tz + timedelta(days=1)

        today_temp, tomorrow_temp = None, None

        # find today's and tomorrow's max temperature
        with allure.step("Find today's and tomorrow's max temperature"):
            for day in forecast.daily:
                date_tz = DateTimeUtils.from_timestamp(day.dt, tz_offset_seconds=tz_offset).date()

                if date_tz == today_date_tz:
                    today_temp = day.temp.max
                if date_tz == tomorrow_date_tz:
                    tomorrow_temp = day.temp.max
                if today_temp is not None and tomorrow_temp is not None:
                    break

        # verify
        with allure.step("Verify temperatures"):
            assert today_temp is not None and tomorrow_temp is not None, "Temperature data not found for today or tomorrow"
            assert today_temp * 0.9 <= tomorrow_temp <= today_temp * 1.1, \
                "Tomorrow's temperature is not within ±10% of ""today's temperature"
