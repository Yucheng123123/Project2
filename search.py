import tweepy
import config

client=tweepy.Client(bearer_token=config.BEARER_TOKEN)

query='yuzuru -is:retweet'

response=client.search_recent_tweets(query=query,max_results=20,expansions=['author_id'])

#users=client.get_liking_users(id=config.TWEET_ID)

#for user in users.data:
#    print(user.username)


for tweet in response.data:
    print(tweet.id)
 #   print(tweet.lang)
