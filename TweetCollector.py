from Tweet import Tweet
from TweetCleaner import TweetCleaner
#from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import csv
import environ
import tweepy
import datetime


class TweetCollector:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)

    def search_tweets(self, query, count=10):
        return self.api.search(query, count=count)

if __name__ == '__main__':
    env = environ.Env(DEBUG=(bool, False), )
    environ.Env.read_env('.env')

    consumer_key = env("CONSUMER_KEY")
    consumer_secret = env("CONSUMER_SECRET")
    access_token = env("ACCESS_TOKEN")
    access_secret = env("ACCESS_SECRET")

    tweet_cleaner = TweetCleaner()
    #factory2 = StopWordRemoverFactory()
    #stopword = factory2.create_stop_word_remover()
    tweetCollector = TweetCollector(consumer_key, consumer_secret, access_token, access_secret)

    tweets_jokowi = []
    tweets_prabowo = []
    print("Starting...")
    jokowi = tweetCollector.search_tweets("Jokowi", count=3200)
    prabowo = tweetCollector.search_tweets("Prabowo", count=3200)

    # Mengambil jangka waktu 10 hari sebelum dan setelah pemungutan suara
    start_date = datetime.datetime(2019, 4, 7)
    end_date = datetime.datetime(2019, 4, 27)
    MAX_TWEETS = 1000

    i_jokowi = 0
    for tweet in jokowi:
        # if tweet.created_at < end_date and tweet.created_at > start_date and i_jokowi < MAX_TWEETS:
        #     tweets_jokowi.append(tweet.text)
        #     i_jokowi += 1
        #     if i_jokowi % 100 == 0: print("Getting Jokowi Tweets:", str(i_jokowi), "of", str(MAX_TWEETS))
        if tweet.text != "":
            tweets_jokowi.append(tweet.text)

    i_prabowo = 0
    for tweet in prabowo:
        # if tweet.created_at < end_date and tweet.created_at > start_date and i_prabowo < MAX_TWEETS:
        #     tweets_prabowo.append(tweet.text)
        #     i_prabowo += 1
        #     if i_prabowo % 100 == 0: print("Getting Prabowo Tweets:", str(i_prabowo), "of", str(MAX_TWEETS))
        if tweet.text != "":
            tweets_prabowo.append(tweet.text)

    with open('jokowi_dataset.txt', 'w', encoding="utf-8") as writer:
        writer.writelines("%s\n" % line for line in tweets_jokowi)
    
    with open('prabowo_dataset.txt', 'w', encoding="utf-8") as writer:
        writer.writelines("%s\n" % line for line in tweets_prabowo)
