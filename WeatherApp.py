from Location import Location
from WeatherService import WeatherService


class WeatherApp:
    def __init__(self):
        self.weather_service = WeatherService()
        self.location = Location()

    def set_location(self, latitude, longitude):
        self.location.set_latitude(latitude)
        self.location.set_longitude(longitude)

    def set_api_key(self, api_key):
        self.weather_service.set_api_key(api_key)

    def get_current_weather(self):
        return self.weather_service.get_weather()

    def get_forecast(self):
        return self.weather_service.get_forecast()
