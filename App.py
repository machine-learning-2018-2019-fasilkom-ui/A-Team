import environ
from textblob import TextBlob
from TweetCollector import TweetCollector


class App:
    def __init__(self):
        self.env = environ.Env(DEBUG=(bool, False), )
        environ.Env.read_env('.env')

        self.consumer_key = self.env("CONSUMER_KEY")
        self.consumer_secret = self.env("CONSUMER_SECRET")
        self.access_token = self.env("ACCESS_TOKEN")
        self.access_secret = self.env("ACCESS_SECRET")


if __name__ == '__main__':
    app = App()

    tweetCollector = TweetCollector(app.consumer_key, app.consumer_secret, app.access_token, app.access_secret)
    jokowi = tweetCollector.search_tweets("Jokowi")
    #print(jokowi)
    #print(tweetCollector.search_tweets("Prabowo"))
    for tweet in jokowi:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        # analysis = analysis.translate(from_lang='id', to='en')
        print(analysis.sentiment)
        if analysis.sentiment[0]>0:
            print('Positive')
        else:
            print('Negative')
        print("")