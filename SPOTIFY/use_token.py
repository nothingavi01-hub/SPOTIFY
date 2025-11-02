import requests
import json

access_token = "BQDUK8UUIYfVRx2z0tkqz762uJgEUcrhFwRfc_7DdgfAV4XM5mT9NrY-HSQSZItjBAvihZmB1hJ4AQPjdwPA4J-s2VM-_sfAoDqkNtW8N5_hVklg-V15ks6W7qSXFTVBQeWdddrk_RRa3PGOOxqrPME9Hc5PRGI-TF5wPVIdvxF3GmdTaUXpbWhY_lY2dnsnbasTaBMpZ3qI2ttFzapKaqbxCA3BYXpHpO85zUCMQBEU9D9Q0gAwom8Ciwy-38DnTwxuUo53-UGF99qSogHAA-3CaHdWpAghJELnOjBOQqmgj0VMVoAqCYPOBeQyn_UGr00d"

url = "https://api.spotify.com/v1/me/player/currently-playing"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    song_name = data["item"]["name"]
    artist_name = data["item"]["artists"][0]["name"]
    progress = data["progress_ms"]
    duration = data["item"]["duration_ms"]
    print(f"🎵 {song_name} — {artist_name}")
    print(f"Progress: {round(progress / duration * 100, 2)}%")
else:
    print("Error:", response.status_code, response.text)
