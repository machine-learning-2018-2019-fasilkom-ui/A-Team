import twitter
import csv
import environ
import datetime
import re

env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')

consumer_key = env("CONSUMER_KEY")
consumer_secret = env("CONSUMER_SECRET")
access_token = env("ACCESS_TOKEN")
access_secret = env("ACCESS_SECRET")

api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

#print(api.VerifyCredentials())
tweets_jokowi = []
tweets_prabowo = []
hashtag_jokowi = ['#JokoWinElection', '#01TheChampion', '#AllahMuliakanJokowi']
hashtag_prabowo = ['#TheVictoryOfPrabowo', '#BesokTusukPrabowoSandi', 'BismillahInsyaAllahPrabowo']
print("Starting...")
jokowi = []
prabowo = []
# Pencoblosan tanggal 17 April 2019, ambil tanggal di sekitar
tanggal_sekitar = ['2019-04-07', '2019-04-08', '2019-04-09', '2019-04-10', '2019-04-11',
    '2019-04-12', '2019-04-13', '2019-04-14', '2019-04-15', '2019-04-16', '2019-04-17',
    '2019-04-18', '2019-04-19', '2019-04-20', '2019-04-21', '2019-04-22', '2019-04-23',
    '2019-04-24', '2019-04-25', '2019-04-26', '2019-04-27']
# Max hanya bisa get 100

print("Getting Jokowi tweets...")
for hashtag in hashtag_jokowi:
    for tanggal in tanggal_sekitar:
        jokowi += api.GetSearch(hashtag, count=100, since=tanggal, until=tanggal)

print("Getting Prabowo tweets...")  
for hashtag in hashtag_prabowo:
    for tanggal in tanggal_sekitar:
        prabowo += api.GetSearch(hashtag, count=100, since=tanggal, until=tanggal)

for tweet in jokowi:
    if tweet.text != "":
        text = tweet.text
        text = re.sub('\n', ' ', text)
        text = text.replace('\n', ' ')
        tweets_jokowi.append(text.strip())


for tweet in prabowo:
    if tweet.text.strip() != "":
        text = tweet.text
        text = re.sub('\n', ' ', text)
        text = text.replace('\n', ' ')
        tweets_prabowo.append(text.strip())

with open('jokowi_dataset.txt', 'w', encoding="utf-8") as writer:
    writer.writelines("%s\n" % line for line in tweets_jokowi)

with open('prabowo_dataset.txt', 'w', encoding="utf-8") as writer:
    writer.writelines("%s\n" % line for line in tweets_prabowo)