import os
from key import YT_KEY
from googleapiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=YT_KEY)

search_response = youtube.search().list(part='snippet', q='요리', type='video').execute()

for item in search_response['items']:
    print(item['snippet']['title'])