import json
import tweepy


class TweetHandler:
    def __init__(self, credentials_filename):
        with open(credentials_filename, "r") as f:
            credentials = json.load(f)
        auth = tweepy.AppAuthHandler(credentials['api_key'], credentials['api_secret_key'])
        self.api = tweepy.API(auth)

    def get_tweets(self, username, count):
        status_objects = self.api.user_timeline(id=username, count=count)
        tweets = []
        for status in status_objects:
            if not status.retweeted:
                tweets.append(status.text)
        return tweets


