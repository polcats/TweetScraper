import tweepy
import csv

from input import *
from timestamp import *
from text_cleaner import *

# You need to register for a twitter dev account to get the keys and tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)  # , wait_on_rate_limit=True

# Creating the API object while passing in auth information
api = tweepy.API(auth)


def scraper_start():
    keyword = get_input("Enter keyword: ", mode=str)
    tweets = scrape_tweets(keyword)
    save_tweets(keyword, tweets)


def scrape_tweets(keyword=None):
    if keyword == None:
        print("No keyword provided")
        return

    tweets = set()
    tweets_count = 0
    try:
        for tweet in tweepy.Cursor(api.search,
                                   q=keyword + " -filter:retweets", tweet_mode='extended',
                                   since="2018-01-01",
                                   # until = "2019-11-111",
                                   # result_type='recent',
                                   # include_entities=True,
                                   # monitor_rate_limit=True,
                                   # wait_on_rate_limit=True,
                                   lang="en",
                                   count=1000).items():
            text = clean_text(tweet.full_text)
            tweets.add("\n" + str(text))
            tweets_count += 1
            print(str(tweets_count))
    except Exception as e:
        print(e)  # 429 = too many requests

    print("\nCollected tweets for " + str(keyword) + ": " + str(len(tweets)))

    return tweets


def save_tweets(file_name, tweets):
    saveFile = open('../data/' + file_name + ' ' +
                    str(date_str) + '.csv', 'a+', encoding="utf-8")

    try:
        for tweet in tweets:
            saveFile.write(str(tweet))
    except:
        pass

    saveFile.close()
