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

# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#             "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, "
#              "you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]