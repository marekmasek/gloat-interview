from pydantic import BaseModel


class LocationByZipResponse(BaseModel):
    zip: str
    name: str
    lat: float
    lon: float
    country: str
