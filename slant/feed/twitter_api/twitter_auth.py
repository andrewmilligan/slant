import os

class TwitterAPIAuth:
  application_id = os.environ['TWITTER_API_APPLICATION_ID']
  application_secret = os.environ['TWITTER_API_APPLICATION_SECRET']
  api_key = ''
