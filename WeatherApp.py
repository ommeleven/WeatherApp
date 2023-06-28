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


class WeatherService:
    def __init__(self):
        self.api_key = ""

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_weather(self):
        # API call and retrieval logic to get the current weather
        return Weather()

    def get_forecast(self):
        # API call and retrieval logic to get the weather forecast
        return [Forecast(), Forecast()]


class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude


class Weather:
    def __init__(self):
        self.temperature = 0.0
        self.description = ""
        self.icon = ""
        self.humidity = 0
        self.wind_speed = 0.0

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_description(self, description):
        self.description = description

    def set_icon(self, icon):
        self.icon = icon

    def set_humidity(self, humidity):
        self.humidity = humidity

    def set_wind_speed(self, wind_speed):
        self.wind_speed = wind_speed


class Forecast:
    def __init__(self):
        self.date_time = ""
        self.temperature = 0.0
        self.description = ""
        self.icon = ""
        self.humidity = 0
        self.wind_speed = 0.0

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_description(self, description):
        self.description = description

    def set_icon(self, icon):
        self.icon = icon

    def set_humidity(self, humidity):
        self.humidity = humidity

    def set_wind_speed(self, wind_speed):
        self.wind_speed = wind_speed
