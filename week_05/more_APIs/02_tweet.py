'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''


import tweepy
from secrets import twitter
import pprint
import json


CAK = twitter['CONSUMER_API_KEY']
CASK = twitter['CONSUMER_API_SECRET_KEY']

AT = twitter['ACCESS_TOKEN']
ATS = twitter['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CAK, CASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

with open('tweets.json', 'r') as f:
    tweets = json.load(f)
    for tweet in tweets:
        api.update_status('tweet')

# DO THIS IN CLI
# ➜  python-onsite git:(master) crontab -e
# crontab: no crontab for ak - using an empty one
#
# at 10.05:
# 5 10 * * * python3 /Users/ak/Documents/_CodingNomads/python-onsite/week_05/more_APIs/02_tweet.py

