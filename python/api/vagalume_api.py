import random

import requests

api_url = "https://api.vagalume.com.br/search.php"


def get_related_artists(artist):
    response = requests.get(
        url=api_url, params={"art": artist, "nolyrics": "1", "extra": "relart"}
    ).json()

    random_artist = random.choice(response["art"]["related"])

    return random_artist["name"]


artist = "Michael Jackson"

for i in range(3):
    artist = get_related_artists(artist)

print(f"Artist of the day: {get_related_artists(artist)} 💿")
print("Powered by https://api.vagalume.com.br/")
