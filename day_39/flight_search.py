import os
import time
import requests
from dotenv import load_dotenv
from datetime import date, timedelta

class FlightSearch:
    
    def __init__(self):
        load_dotenv("./.venv/.env")
        self.client_id = os.getenv("AMADEUS_API_KEY")
        self.client_secret = os.getenv("AMADEUS_API_SECRET")
        self.access_token = self.get_access_token()
        self.header = {"Authorization": f"Bearer {self.access_token}"}
        
    def get_access_token(self):
        """
        return access_token: str
        """
        AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_header = {"Content-Type": "application/x-www-form-urlencoded"}
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(AUTH_ENDPOINT, headers=auth_header, data=auth_data)
        
        if "access_token" in response.json():
            return response.json()['access_token']
        else:
            print("Error trying to get access_token:")
            response.raise_for_status()
        
    def get_destination_code(self, city):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url= "https://test.api.amadeus.com/v1/reference-data/locations/cities",
            headers= headers,
            params= params
        )
        print(f"Status code {response.status_code}.")
        try:
            code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return None
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return None
        return code
    
    def get_flight_data(self, destination_code, year, month, delta_time):
        FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        cheapest_flight_month = None
        min_price_month = float('inf')
        
        start_date_month = date(year, month, 1)
        if month == 12:
            end_date_month = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            end_date_month = date(year, month + 1, 1) - timedelta(days=1)
            
        current_date = start_date_month
        while current_date <= end_date_month:
            print(f"Analysing current data: {current_date.strftime("%Y-%m-%d")}")
            
            params = {
                "originLocationCode": "BSB",
                "destinationLocationCode": destination_code,
                "departureDate": current_date.strftime("%Y-%m-%d"),
                "adults": 1
            }
            response = requests.get(FLIGHT_OFFERS_ENDPOINT, headers=self.header, params=params)
            data = response.json()

            if "data" in data:
                for offer in data["data"]:
                    price_str = offer.get("price", {}).get("total")
                    if price_str:
                        try:
                            price = float(price_str)
                            if price < min_price_month:
                                min_price_month = price
                                cheapest_flight_month = {
                                    "date": current_date.strftime("%Y-%m-%d"),
                                    "price": price,
                                    "offer_details": offer
                                }
                        except ValueError:
                            print(f"Float Error '{price_str}'.")
            elif "errors" in data:
                print(f"Error searching for [{current_date}]: {data['errors']}")

            time.sleep(2)
            current_date += timedelta(days=delta_time)

        if cheapest_flight_month:
            cheap_text = f"The cheapest BSB - {destination_code} flight in  {month}/{year} (each {delta_time} days) is:\nDate: {cheapest_flight_month['date']}\nPrice: {cheapest_flight_month['price']}"
            print(cheap_text)
            return cheap_text
        else:
            print(f"No BSB - {destination_code} flights in {month}/{year}")
            return None