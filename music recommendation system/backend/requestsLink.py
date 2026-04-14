import requests
import re

def recommend(song_name):
        
    query = "song_name " + song_name
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    html = requests.get(search_url, headers=headers).text

    # video IDs nikaal
    video_ids = re.findall(r"watch\?v=(\S{11})", html)

    # first unique video
    video_ids = list(dict.fromkeys(video_ids))

    if video_ids:
        link = "https://www.youtube.com/watch?v=" + video_ids[0]
    else:
        link = "No video found"

    return link