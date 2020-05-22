import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# It allows us to hit twitter api
def limit_handler(curdor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)
	

# generous bot...It will follow back to my twitter follower
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	# If i want to follow someone by their follower count
	if follower.followers_count > 100:
		follower.follow()
		break

	# In here i am going to folloe back someone by bot
	#if follower.name == 'Rezaul':
		#follower.follow()
		#break




