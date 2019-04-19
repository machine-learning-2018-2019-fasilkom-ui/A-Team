class Tweet:
    def __init__(self, tweet, who, score):
        self.tweet = tweet
        self.who = who
        self.score = score

    def __str__(self):
        return self.tweet + " - " + self.who + " - " + str(self.score)

    def __iter__(self):
        return iter([self.tweet, self.who, str(self.score)])
