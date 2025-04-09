import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv("./.venv/.env")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

def check_if_day(current_time: str, sunrise: str, sunset: str) -> bool:
    try:
        format = "%H:%M:%S"
        time = dt.datetime.strptime(current_time, format).time()
        rise = dt.datetime.strptime(sunrise, format).time()
        set = dt.datetime.strptime(sunset, format).time()

        return rise <= time <= set

    except ValueError:
        print("Error: String invalid format (HH:MM:SS).")

def is_iss_overhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    
    return (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LONG-5 <= iss_long <= MY_LONG+5)

params = {
    "lat":MY_LAT,
    "lng":MY_LONG,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split()[0].split(":")
sunrise[0] = str(int(sunrise[0]) - 3)
sunrise = ":".join(sunrise)
sunset = data["results"]["sunset"].split()[0].split(":")
sunset[0] = str(int(sunset[0]) - 3 + 12)
sunset = ":".join(sunset)

now = dt.datetime.now()
time_now = now.time()
time_now = str(time_now).split(".")[0]

if not check_if_day(time_now, sunrise, sunset) and is_iss_overhead():
    print("LOOK UP NOW!!")
else:
    print("not yet :/")