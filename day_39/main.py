import time
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

def add_wish_city(new_city):
        iata = flight_search.get_destination_code(new_city)
        if iata != None:
                data_manager.add_city(new_city, iata)

def check_price():
        data_manager.list_cities()
        iata = input("\nWhat city would you like to check price? (IATA code) ")
        year = int(input("In what year? "))
        month = int(input("What month? "))
        delta_time = int(input("delta_time: "))
        
        flight_text = flight_search.get_flight_data(iata, year, month, delta_time)
        if flight_text != None:
                if input("Would you like to receive this as a WhatsApp msg? (yes/no) ").lower() == 'yes':
                        whatsapp = NotificationManager()
                        whatsapp.send_msg(flight_text)

while True:
    print(
            "Choose an option:\n"
            "1 - List all cities saved\n"
            "2 - Check prices\n"
            "3 - Add a new wish city\n"
            "4 - Leave"
        )
    user_input = input("Enter your choice (1-3): ")
    print("\n")
    if user_input in ['1', '2', '3', '4']:
        break  
    else:
        print("Invalid input. Please enter a number between 1 and 3.")
        
data_manager = DataManager()
flight_search = FlightSearch()

match user_input:
        case '1':
                data_manager.list_cities()
        case '2':
                check_price()
        case '3':
                add_wish_city(input("What city would you like to add to the list? "))
        case '4':
                print("Bye :)")
