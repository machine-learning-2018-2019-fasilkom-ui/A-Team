from Tweet import Tweet
from TweetCleaner import TweetCleaner
from TweetCollector import TweetCollector
from Sastrawi.StopWordRemover.StopWordRemoverFactory import \
    StopWordRemoverFactory

from sklearn.feature_extraction.text import CountVectorizer
import environ

jokowi_tweets = []
prabowo_tweets = []

for line in open('jokowi_dataset.txt', 'r'):
    jokowi_tweets.append(line.strip())

for line in open('prabowo_dataset.txt', 'r'):
    prabowo_tweets.append(line.strip())

cv = CountVectorizer(binary=True)
cv.fit(jokowi_tweets)
X = cv.transform(jokowi_tweets)
# Implemented later
# X_test = cv.transform(jokowi_tweets_test)
print(X)
