# HTTP Requests
# requests.get()
# requests.post()
# requests.put()
# request.delete()
import os
import requests
from dotenv import load_dotenv

load_dotenv("./.venv/.env")
MY_TOKEN = os.getenv("TOKEN")

header = {
    "X-USER-TOKEN": MY_TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
   "token": MY_TOKEN,
   "username": "budabecker",
   "agreeTermsOfService": "yes",
   "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/budabecker/graphs"
graph_config = {
    "id": "codingstudy",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ichou",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = "https://pixe.la/v1/users/budabecker/graphs/codingstudy"
pixel_config = {
    "date": "20250408",
    "quantity": "5",
}
# response = requests.post(url=pixel_endpoint, headers=header, json=pixel_config)
# print(response)