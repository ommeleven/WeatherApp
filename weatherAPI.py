import requests

# get
apiKey = "36bab58ca3e8543ac064974051023e67"
cityName = "Chicago"
countryCode = "US"
res = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial"
)
currTemp = res.json()["main"]["temp"]
