import requests
#from flask import Flask, render_template

#app = Flask('testapp')

# get
apiKey = "36bab58ca3e8543ac064974051023e67"
cityName = "Chicago"
countryCode = "US"
res = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={cityName},{countryCode}&appid={apiKey}&units=imperial")

currTemp = res.json()
#@app.route('/')
#def index():
 #   return render_template('index.html', variable='currTemp')

#print(type(currTemp))
#for c in currTemp.items():
    #print((c)) 
print(len(currTemp))
HTML = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Download</title>
</head>
<body>
    <pre>
    My first weather app 
    city: {cityName}
    temperature: {currTemp['main']['temp']}
    </pre>
</body>
</html>
'''
with open('index.html','w') as f:
    f.write(HTML)  

#if __name__ == '__main__':
#    app.run() 
