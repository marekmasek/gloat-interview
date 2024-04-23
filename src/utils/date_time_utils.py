from datetime import timedelta, datetime


class DateTimeUtils:

    @staticmethod
    def now(tz_offset_seconds: int = None) -> datetime:
        """
        Get the current datetime with a specified timezone offset.

        Args:
            tz_offset_seconds: The timezone offset in seconds
        """
        current_dt = datetime.now()
        if tz_offset_seconds is not None:
            current_dt += timedelta(seconds=tz_offset_seconds)
        return current_dt

    @staticmethod
    def from_timestamp(timestamp: int, tz_offset_seconds: int = None) -> datetime:
        """
        Converts a Unix UTC timestamp to a datetime object with adding timezone offset in seconds

        Args:
            timestamp: The Unix timestamp to convert.
            tz_offset_seconds: The timezone offset in seconds which will be added to the timestamp.
        """
        dt = datetime.utcfromtimestamp(timestamp)
        if tz_offset_seconds is not None:
            dt += timedelta(seconds=tz_offset_seconds)
        return dt
