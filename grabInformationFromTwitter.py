import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#1.public_tweets = api.home_timeline()
#1.for tweet in public_tweets:
	#1. print(tweet.text)

#2. user = api.me()
#2. print(api.name)
#2. PRINT(api.screen_name)
#2. print(api.followers_count)




