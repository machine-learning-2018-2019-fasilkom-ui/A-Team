import environ

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
    print(tweetCollector.search_tweets("Jokowi"))
    print(tweetCollector.search_tweets("Prabowo"))
