import googleapiclient.discovery
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# API client library
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = os.getenv('API_KEY')
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# request = youtube.search().list(
#     part="id,snippet",
#     type='video',
#     maxResults=1,
#     fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
# )

videoRequest = youtube.videos().list(
    part="id,snippet",
    chart="mostPopular",
    maxResults=1,
    fields="items(id,snippet(publishedAt,channelId,channelTitle,title,description,categoryId))"
)

videoCategoryRequest = youtube.videoCategories().list(
    part="id,snippet",
    id="1,2,3,4,5,6,7,8,9,10",
    fields="items(id,snippet(channelId,title))"
)

# Query execution
video_response = videoRequest.execute()


# Print the results
print(video_response)

video_category_response = videoCategoryRequest.execute()

print(video_category_response)
