'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy
from secrets import twitter

CAK = twitter['CONSUMER_API_KEY']
CASK = twitter['CONSUMER_API_SECRET_KEY']

AT = twitter['ACCESS_TOKEN']
ATS = twitter['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CAK, CASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

followers = api.followers('SjannekedeCrom')

few_followers = {}
many_followers = {}


for follower in followers:
    if follower.followers_count < 500:
        few_followers[follower.screen_name] = f" Ratio friends/followers: {round(follower.friends_count/follower.followers_count, 1)}"
    else:
        many_followers[follower.screen_name] = f" Ratio friends/followers: {round(follower.friends_count/follower.followers_count, 1)}"

print(few_followers)
print(many_followers)

