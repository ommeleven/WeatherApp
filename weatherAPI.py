import requests
# get
apiKey = "36bab58ca3e8543ac064974051023e67"
cityName = "Chicago"
countryCode = "US"
url = "https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial"



 
class WeatherAPI:

    apiKey = "36bab58ca3e8543ac064974051023e67"
    cityName = input("Whih city do you live in? ")
    countryCode = "US"
    currWeather = ''
    url = "https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial"

    def get_weather_data(self, location):
        pass
        
    def make_api_request(self):
        # network requests to external API
        res = requests.get(url=url)
        currWeather = res.json()
        print(currWeather)

APIcall = WeatherAPI()
APIcall.make_api_request()