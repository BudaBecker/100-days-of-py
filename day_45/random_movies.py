import random
import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_text = BeautifulSoup(response.text, "html.parser")
titles = html_text.find_all(name="h3", class_="title")

movie_rank = []
for rank in titles:
    lista = rank.text.split(") ")
    try:
        movie_rank.append((int(lista[0]) ,lista[1]))
    except:
        lista = rank.text.split(": ")
        movie_rank.append((int(lista[0]) ,lista[1]))
    
movie = random.choice(movie_rank)

print(f"Today's movie is: {movie[1]}, top{movie[0]}")