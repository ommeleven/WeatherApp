from weather_service import WeatherService
from location_manager import LocationManager
from clothing_recommendation import ClothingRecommendation
from user_interface import UserInterface

class ApplicationController:
    def __init__(self):
        self.weather_service = WeatherService()
        self.location_manager = LocationManager()
        self.clothing_recommendation = ClothingRecommendation()
        self.user_interface = UserInterface()

    def start_app(self):
        self.user_interface.handle_user_input("initialize")

    # Other methods from the previous code
    # Hello :)