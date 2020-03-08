import sys

from pymongo import MongoClient, DESCENDING

from key import YT_KEY
from googleapiclient.discovery import build


def show_top_videos(collection):
    for item in collection.find().sort('statistics.viewCount', DESCENDING).limit(5):
        print(item['statistics']['viewCount'], item['snippet']['title'])


def main():
    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.scraping.videos

    # 모든 문서 삭제
    collection.delete_many({})

    for items_per_page in search_videos('요리'):
        save_to_mongodb(collection, items_per_page)
        
    show_top_videos(collection)

    
def search_videos(q, max_pages=2):
    youtube = build('youtube', 'v3', developerKey=YT_KEY)

    search_request = youtube.search().list(part='id', q=q, type='video', maxResults=50)

    i = 0

    while search_request and i < max_pages:
        search_response = search_request.execute()

        video_ids = [item['id']['videoId'] for item in search_response['items']]

        video_response = youtube.videos().list(part='snippet, statistics', id=','.join(video_ids)).execute()

        yield video_response['items']

        search_request = youtube.search().list_next(search_request, search_response)
        i += 1


def save_to_mongodb(collection, items):

    if not items:
        return

    for item in items:
        item['_id'] = item['id']

        for key, value in item['statistics'].items():
            item['statistics'][key] = int(value)

    result = collection.insert_many(items)

    print("Inserted {0} documents".format(len(result.inserted_ids)), file=sys.stderr)

if __name__ == '__main__':
    main()
