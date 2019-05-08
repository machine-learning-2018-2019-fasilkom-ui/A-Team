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
for i in hashtag_jokowi:
    jokowi += api.GetSearch(i, count=320)
for i in hashtag_prabowo:
    prabowo += api.GetSearch(i, count=320)
i_jokowi = 0
for tweet in jokowi:
    # if tweet.created_at < end_date and tweet.created_at > start_date and i_jokowi < MAX_TWEETS:
    #     tweets_jokowi.append(tweet.text)
    #     i_jokowi += 1
    #     if i_jokowi % 100 == 0: print("Getting Jokowi Tweets:", str(i_jokowi), "of", str(MAX_TWEETS))
    if tweet.text != "":
        text = tweet.text
        text = re.sub('\n', ' ', text)
        tweets_jokowi.append(tweet.text.strip())

i_prabowo = 0
for tweet in prabowo:
    # if tweet.created_at < end_date and tweet.created_at > start_date and i_prabowo < MAX_TWEETS:
    #     tweets_prabowo.append(tweet.text)
    #     i_prabowo += 1
    #     if i_prabowo % 100 == 0: print("Getting Prabowo Tweets:", str(i_prabowo), "of", str(MAX_TWEETS))
    if tweet.text.strip() != "":
        text = tweet.text
        text = re.sub('\n', ' ', text)
        tweets_prabowo.append(tweet.text.strip())

tweets_jokowi = [line for line in tweets_jokowi if line.strip() != '']
tweets_prabowo = [line for line in tweets_prabowo if line.strip() != '']

with open('jokowi_dataset.txt', 'w', encoding="utf-8") as writer:
    writer.writelines("%s\n" % line.strip() for line in tweets_jokowi)

with open('prabowo_dataset.txt', 'w', encoding="utf-8") as writer:
    writer.writelines("%s\n" % line.strip() for line in tweets_prabowo)