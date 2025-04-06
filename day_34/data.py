import requests
import time

params_1 = {
    "amount": 5,
    "category": 18,
    "type": "boolean",
}
response_1 = requests.get(url="https://opentdb.com/api.php", params=params_1)
response_1.raise_for_status()
data_comp = response_1.json()

time.sleep(5)
params_2 = {
    "amount": 5,
    "category": 19,
    "type": "boolean",
}
response_2 = requests.get(url="https://opentdb.com/api.php", params=params_2)
response_2.raise_for_status()
data_math = response_2.json()

question_data = data_comp["results"] + data_math["results"]