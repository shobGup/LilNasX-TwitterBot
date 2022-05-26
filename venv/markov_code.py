import markovify
from twython import Twython
import tweepy
from time import sleep

API_KEY = 'ehpLGSmcQIayMRVsr5QcTDK8H'
API_SECRET = 'IITy6RhyuH4xYq27PBjQPClFXEfM46rgDLfSVtIvikEhlT9sOC'
ACCESS_TOKEN = '1528939374926340098-LjtuQa3NxgvV0ItzBS8DaxE9wYK48i'
ACCESS_SECRET = 'yWm7zNdkNqTsvLAuvDGDVeOWiHpEAQW7SKaP60shx0uVh'
twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


with open("/Users/shobhit/PycharmProjects/TwitterBot/corpus3.txt") as f:
    text = f.read()

text_model = markovify.Text(text)
tweet = text_model.make_short_sentence(280)

while True:
    tweet = text_model.make_short_sentence(280)
    print("About to tweet:", tweet)
    sleep(28512)

    twitter.update_status(status=tweet)

