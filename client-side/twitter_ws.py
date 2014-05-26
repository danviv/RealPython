#twitter api example
#Twitter Web Services

import tweepy

consumer_key = "<get from twitter>"
consumer_secret = "<get from twitter>"
access_token = "<get from twitter>"
access_secret ="<get from twitter>"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
tweets = api.search(q='#USDINR futures')

#display results to screen
for t in tweets:
	print t.created_at, t.text, "\n"