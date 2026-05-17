import requests
from bs4 import BeautifulSoup
from rich import print as prettyprint
from ytmusicapi import YTMusic

date = input(
    "which year do you want to travel to ? Type date in this format yyyy-mm-dd:"
)
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"

response = requests.get(url=url)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
song_titles_elements = soup.find_all(name="h3", class_="chart-entry__title")

song_titles = [song.text for song in song_titles_elements]

yt = YTMusic("./browser.json")

playlist_name = f"{date} billboard 100"
playlist = yt.create_playlist(playlist_name, description="bootcamp project")

for song in song_titles:
    try:
        matched_song = yt.search(query=song, filter="songs")
        matched_song_id = matched_song[0]["videoId"]
    except Exception as e:
        print("Error searching song")
        print(f"reason: {e}")
    else:
        matched_song = yt.search(query=song, filter="songs")
        matched_song_id = [matched_song[0]["videoId"]]
        yt.add_playlist_items(playlistId=str(playlist), videoIds=matched_song_id)
        print(f"song added: {song}")
