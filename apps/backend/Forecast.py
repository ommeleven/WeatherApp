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
