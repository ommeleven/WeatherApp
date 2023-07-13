import Forecast, Weather  # noqa: E401


class WeatherService:
    def __init__(self):
        self.api_key = "36bab58ca3e8543ac064974051023e67"

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_weather(self):
        # API call and retrieval logic to get the current weather
        return Weather()

    def get_forecast(self):
        # API call and retrieval logic to get the weather forecast
        return [Forecast(), Forecast()]
