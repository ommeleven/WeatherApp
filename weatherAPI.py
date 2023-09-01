import requests
# get
apiKey = "36bab58ca3e8543ac064974051023e67"
cityName = "Chicago"
countryCode = "US"


 
class WeatherAPI:
    apiKey = "36bab58ca3e8543ac064974051023e67"
    cityName = input("Whih city do you live in? ")
    countryCode = "US"
    currWeather = ''
    def get_weather_data(self, location):
        pass
        
    def make_api_request(self, url):
        # network requests to external API
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial")
        currWeather = res.json()

    print(currWeather)

WeatherAPI()