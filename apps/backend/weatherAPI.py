import requests


class WeatherAPI:
    apiKey = "5f0a2784fd6e5677b3acf53cb1a46274"
    cityName = "Chicago"
    countryCode = "US"
    currWeather = ""

    def get_weather_data(self, location):
        pass

    def make_api_request(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.cityName},{self.countryCode}&appid={self.apiKey}&units=imperial"
        res = requests.get(url)
        currWeather = res.json()
        return currWeather


if __name__ == "__main__":
    APIcall = WeatherAPI()
    weather_data = APIcall.make_api_request()
    if weather_data:
        print("Weather data:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve weather data.")
