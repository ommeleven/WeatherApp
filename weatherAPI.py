import requests 
class WeatherAPI:

    apiKey = "5f0a2784fd6e5677b3acf53cb1a46274"
    cityName = input("here Which city do you live in? ")
    countryCode = "US"
    currWeather = ''
    url = "https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial"
    r = requests.get(url)
    print(r.json())

    def get_weather_data(self, location):
        pass
        
    def make_api_request(self):
        # network requests to external API
        res = requests.get(self.url)
        currWeather = res.json()
        print('currWeather: ', currWeather)
        return currWeather
    

#APIcall = WeatherAPI()
#APIcall.make_api_request()