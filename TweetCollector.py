from Tweet import Tweet
from TweetCleaner import TweetCleaner
from Sastrawi.StopWordRemover.StopWordRemoverFactory import \
    StopWordRemoverFactory

import csv
import environ
import tweepy


class TweetCollector:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)

    def search_tweets(self, query):
        return self.api.search(query)

if __name__ == '__main__':
    env = environ.Env(DEBUG=(bool, False), )
    environ.Env.read_env('.env')

    consumer_key = env("CONSUMER_KEY")
    consumer_secret = env("CONSUMER_SECRET")
    access_token = env("ACCESS_TOKEN")
    access_secret = env("ACCESS_SECRET")

    tweet_cleaner = TweetCleaner()
    factory2 = StopWordRemoverFactory()
    stopword = factory2.create_stop_word_remover()
    tweetCollector = TweetCollector(consumer_key, consumer_secret, access_token, access_secret)

    tweets_jokowi = []
    tweets_prabowo = []

    jokowi = tweetCollector.search_tweets("Jokowi")
    prabowo = tweetCollector.search_tweets("Prabowo")

    jokowi = tweetCollector.search_tweets("Jokowi")
    prabowo = tweetCollector.search_tweets("Prabowo")

    for tweet in jokowi:
        text = stopword.remove(tweet.text)
        text = tweet_cleaner.clean(text)
        tweets_jokowi.append(text)

    for tweet in prabowo:
        text = stopword.remove(tweet.text)
        text = tweet_cleaner.clean(text)
        tweets_prabowo.append(text)

    with open('jokowi_dataset.txt', 'w') as writer:
        writer.writelines("%s\n" % line for line in tweets_jokowi)
    
    with open('prabowo_dataset.txt', 'w') as writer:
        writer.writelines("%s\n" % line for line in tweets_prabowo)
