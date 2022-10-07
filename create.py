import tweepy
import config

client=tweepy.Client(consumer_key=config.API_KEY,
                     consumer_secret=config.API_SECRET,
                     access_token=config.ACCESS_TOKEN,
                     access_token_secret=config.ACCESS_TOKEN_SECRET)

#response=client.create_tweet(text="yuzuru hanyu's best performance",poll_duration_minutes=5,poll_options=['seimei','h&l','pw'])

response=client.create_tweet(text="yuzuru hanyu")

print(response)