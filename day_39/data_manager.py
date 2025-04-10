import os
import requests
from dotenv import load_dotenv

class DataManager:
    
    def __init__(self):
        load_dotenv("./.venv/.env")
        self.sheet_endpoint = f"https://api.sheety.co/{os.getenv("SHEET_CODE")}/pythonFlightDeals/prices"

    def list_cities(self):
        sheet_response = requests.get(self.sheet_endpoint)
        sheet_response.raise_for_status()
        if sheet_response.status_code != 200:
            print("API Error")
        else:
            for cities in sheet_response.json()["prices"]:
                print(f"{cities["city"]}, {cities["iataCode"]}")
                
    def add_city(self, city, iata):
        params = {
            "price": {
                "city": city,
                "iataCode": iata,
            }
        }
        sheet_response = requests.post(self.sheet_endpoint, json=params)
        print(f"Status code {sheet_response.status_code}.")