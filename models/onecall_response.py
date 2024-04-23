from typing import List, Optional

from pydantic import BaseModel


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainData(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    weather: List[Weather]


class ForecastMinutelyItem(BaseModel):
    dt: int
    precipitation: int


class ForecastHourlyItem(BaseModel):
    dt: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float] = None
    weather: List[Weather]
    pop: float


class Temp(BaseModel):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


class FeelsLike(BaseModel):
    day: float
    night: float
    eve: float
    morn: float


class DailyItem(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    moonrise: int
    moonset: int
    moon_phase: float
    summary: str
    temp: Temp
    feels_like: FeelsLike
    pressure: int
    humidity: int
    dew_point: float
    wind_speed: float
    wind_deg: int
    wind_gust: float
    weather: List[Weather]
    clouds: int
    pop: float
    rain: Optional[float] = None
    uvi: float


class Alert(BaseModel):
    sender_name: str
    event: str
    start: int
    end: int
    description: str
    tags: List[str]


class OneCallResponse(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: MainData
    minutely: List[ForecastMinutelyItem]
    hourly: List[ForecastHourlyItem]
    daily: List[DailyItem]
    alerts: Optional[List[Alert]] = None
