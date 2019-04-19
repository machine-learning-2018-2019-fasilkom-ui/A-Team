import csv

import environ
from textblob import TextBlob

from Tweet import Tweet
from TweetCleaner import TweetCleaner
from TweetCollector import TweetCollector
from Sastrawi.StopWordRemover.StopWordRemoverFactory import \
    StopWordRemoverFactory  # untuk menghilangkan stopword /kata sambung


class ComparisonGenerator:
    def __init__(self):
        self.env = environ.Env(DEBUG=(bool, False), )
        environ.Env.read_env('.env')

        self.consumer_key = self.env("CONSUMER_KEY")
        self.consumer_secret = self.env("CONSUMER_SECRET")
        self.access_token = self.env("ACCESS_TOKEN")
        self.access_secret = self.env("ACCESS_SECRET")


if __name__ == '__main__':
    comparison_generator = ComparisonGenerator()
    tweet_cleaner = TweetCleaner()
    factory2 = StopWordRemoverFactory()
    stopword = factory2.create_stop_word_remover()
    tweetCollector = TweetCollector(comparison_generator.consumer_key, comparison_generator.consumer_secret,
                                    comparison_generator.access_token, comparison_generator.access_secret)

    jokowi = tweetCollector.search_tweets("Jokowi")
    prabowo = tweetCollector.search_tweets("Prabowo")

    tweets = []

    for tweet in jokowi:
        text = stopword.remove(tweet.text)
        text = tweet_cleaner.clean(text)
        analysis = TextBlob(text)
        # analysis = analysis.translate(from_lang='id', to='en')

        tweets.append(Tweet(text, "jokowi", analysis.sentiment[0]))

    for tweet in prabowo:
        text = stopword.remove(tweet.text)
        text = tweet_cleaner.clean(text)
        analysis = TextBlob(text)
        # analysis = analysis.translate(from_lang='id', to='en')

        tweets.append(Tweet(text, "prabowo", analysis.sentiment[0]))

    for tweet in tweets:
        print(list(tweet))

    with open('comparison_data.csv', 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        for tweet in tweets:
            wr.writerow(list(tweet))
