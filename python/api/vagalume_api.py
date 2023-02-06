import random

import requests

api_url = "https://api.vagalume.com.br/search.php"


def get_related_artists(artist):
    response = requests.get(
        url=api_url, params={"art": artist, "nolyrics": "1", "extra": "relart"}
    ).json()

    random_artist = random.choice(response["art"]["related"])

    return random_artist


artist = {
    "name": "Michael Jackson"
}

for i in range(3):
    artist = get_related_artists(artist["name"])

print(f"Artist of the day: {artist['name']} 💿")
print(f"More info: {artist['url']}")

print("\n Powered by https://api.vagalume.com.br/")
