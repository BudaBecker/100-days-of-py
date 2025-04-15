import requests
from bs4 import BeautifulSoup


date = "2025-04-12"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response  = requests.get(f"https://www.billboard.com/charts/hot-100/{date}", headers=header)

html_text = BeautifulSoup(response.text, "html.parser")

song_names_spans = html_text.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names) 