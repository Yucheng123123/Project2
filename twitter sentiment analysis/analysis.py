import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
class Twitter_User(object):
   def __init__(self):
      consumer_key = 'MNjVsWBuINDdWxx9A4hFEHmvT'
      consumer_secret = 'xtgI6rg2Jcd0I8KjeyFZTh1PKMaBrHJcPCZA2RHMxvwtgoEmkN'
      access_token = '1577736170212950017-to2AOGt32CqYfIB1Ycboz0MzI5vuMJ'
      access_token_secret = 'ZUICchF0w76OKEevaLybC10bqnoLexVLAnvJBRml8okhe'
      try:
         self.auth = OAuthHandler(consumer_key, consumer_secret)
         self.auth.set_access_token(access_token, access_token_secret)
         self.api = tweepy.API(self.auth)
      except:
         print("Error: Authentication Failed")
   def pristine_tweet(self, twitter):
      return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", twitter).split())
   def Sentiment_Analysis(self, twitter):
      audit = TextBlob(self.pristine_tweet(twitter))
      # set sentiment
      if audit.sentiment.polarity > 0:
         return 'positive'
      elif audit.sentiment.polarity == 0:
         return 'negative'
   def tweet_analysis(self, query, count = 10):
      twitter_tweets = []
      try:
         get_twitter = self.api.search_tweets(q = query, count = count)
         for tweets in get_twitter:
            inspect_tweet = {}
            inspect_tweet['text'] = tweets.text
            inspect_tweet['sentiment'] = self.Sentiment_Analysis(tweets.text)
            if tweets.retweet_count > 0:
               if inspect_tweet not in twitter_tweets:
                  twitter_tweets.append(inspect_tweet)
               else:
                  twitter_tweets.append(inspect_tweet)
         return twitter_tweets
      except tweepy.errors.TweepyException as e:
         print("Error : " + str(e))
def main():
   api = Twitter_User()
   twitter_tweets = api.tweet_analysis(query = 'Yuzuru', count = 200)
   Positive_tweets = [tweet for tweet in twitter_tweets if tweet['sentiment'] == 'positive']
   print("Positive tweets percentage: {} %".format(100*len(Positive_tweets)/len(twitter_tweets)))
   Negative_tweets = [tweet for tweet in twitter_tweets if tweet['sentiment'] == 'negative']
   print("Negative tweets percentage: {} %".format(100*len(Negative_tweets)/len(twitter_tweets)))
   print("\n\nPositive_tweets:")
   for tweet in Positive_tweets[:10]:
      print(tweet['text'])
   print("\n\nNegative_tweets:")
   for tweet in Negative_tweets[:10]:
      print(tweet['text'])
if __name__ == "__main__":
   main()
