import tweepy


class TweetCollector:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)

    def search_tweets(self, query):
        return self.api.search(query)
