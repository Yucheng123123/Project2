# Project2
## Search Tweets
This section tests how to get tweets for certain keywords for the past 7 days. First you need to log in to _developer.twitter.com_ to create a new app, then get a token and password.

![doc](https://user-images.githubusercontent.com/113315434/194594323-a4d2483b-9f67-4e68-958b-cb6317aeea6f.PNG)

The API token allowed me to programmatically connect to Twitter's APIs. 

Token consists of two parts

_Token: The public part of the credential. It is often referred to as a username or access key during authentication. (It's named **ACCESS_TOKEN** here)_

_Password: The private part of the credential. Usually referred to as the password or access code during authentication. (It's named **ACCESS_SECRET** here)_

The name "**BEARER_TOKEN**" can be understood as "granting access to the holder of this token". Bearer tokens allowed me to have a more secure entry point for using the Twitter API.

To get user IDs and usernames I found the _expansions_ in the Twitter API doc.

![expansion](https://user-images.githubusercontent.com/113315434/194600823-ab1466f1-e569-4351-9787-b2a348cd881d.PNG)

"author_id" was what needed to be added into parameters.
### Test Program
_import tweepy_

_import config_

_client=tweepy.Client(bearer_token=config.BEARER_TOKEN)_

_query='yuna kim -is:retweet'_

_response=client.search_recent_tweets(query=query,expansions=['author_id'])_

_users={u['id']:u for u in response.includes['users']}_

_for tweet in response.data:_

    if users[tweet.author_id]:

        user=users[tweet.author_id]

        print(tweet.id)

        print(user.username)
### Result
![image](https://user-images.githubusercontent.com/113315434/194598204-145c3c52-3a3e-41a1-a059-8dcd4c27b209.png)

Entering debug mode returned 10 tweets, including the keyword 'yuna kim'.

To get more tweets, I added the max_results parameter to specify the maximum number of tweets to get at a time.

![image](https://user-images.githubusercontent.com/113315434/194598647-40964783-eb99-42c4-8d3a-5c396e71ba1c.png)

Now the number of data becomes 20, which means that 20 tweets are fetched.

If I changed the keyword to "yuzuru", the data returned would also changed:

![image](https://user-images.githubusercontent.com/113315434/194599230-a53280f6-7fa1-4b31-bbcf-d5e00922f6bd.png)

Run the program to print the user IDs and usernames of the tweet.

![image](https://user-images.githubusercontent.com/113315434/194598820-ed51d32f-68da-4612-bed0-68fc548af117.png)

## Get the language of tweets
On top of getting the users of the tweets, I also wanted to get the language used in the tweets. 

So, I added tweet_fields as a parameter.
### Test Program
_import tweepy_

_import config_

_client=tweepy.Client(bearer_token=config.BEARER_TOKEN)_

_query='yuzuru -is:retweet'_

_response=client.search_recent_tweets(query=query,tweet_fields=['created_at','lang'])_

_for tweet in response.data:_

    print(tweet.id)
    
    print(tweet.lang)
### Result
![lang](https://user-images.githubusercontent.com/113315434/194601315-2b7cf5e7-0633-4fa9-b279-42bb5259bdb6.PNG)

It showed that the first tweet was written in Korean and the second one was written in English.

## Get users who liked one tweet
This part is great. Usually whenever I want to check the users who liked a tweet, it's always very annoying because there are too many people who liked it. This section tests how to get all the users who have liked a tweet.
### Test Program
_import tweepy_

_import config_

_client=tweepy.Client(bearer_token=config.BEARER_TOKEN)_

_users=client.get_liking_users(id=config.TWEET_ID)_

_for user in users.data:_

_print(user.username)_
### Result
This section introduced TWEET_ID, which is a unique ID identifier for each tweet.

![194589508-b4e70a22-fcb7-4cd2-8d54-e92611710da4](https://user-images.githubusercontent.com/113315434/194592116-bbf05007-2393-427e-9aff-4437e792bb9a.png)

If I changed TWEET_ID in config.py to get users who liked another tweet:

![194590008-10ab4111-2e5a-4840-9901-bc1f5a9ac755](https://user-images.githubusercontent.com/113315434/194592157-d3cf725f-532a-4271-b8cc-b3f5ec97e1db.png)

![194590093-baef095b-775b-46af-a1de-631d09338c06](https://user-images.githubusercontent.com/113315434/194592202-a6c44e22-818a-4386-9416-7d92604e4a5a.png)

I got another list of username.
### Problems to be solved
On top of that I would like to go a step further and get the names of the users who liked any of the several or hundreds of tweets at once and have them automatically sorted.

## Write a tweet
In this section I wanted to test how to send tweets. I needed to create a new client.

![image](https://user-images.githubusercontent.com/113315434/194604120-e5668847-82eb-4445-be0d-60faffea703e.png)

With this client, I can send tweets through the test program.
### Test Program
_import tweepy_

_import config_

_client=tweepy.Client(consumer_key=config.API_KEY,_
                     _consumer_secret=config.API_SECRET,_
                     _access_token=config.ACCESS_TOKEN,_
                     _access_token_secret=config.ACCESS_TOKEN_SECRET)_

_response=client.create_tweet(text="yuzuru hanyu")_

_print(response)_
### Result
![test-create](https://user-images.githubusercontent.com/113315434/194604513-a5a7bbbe-edc8-4aa9-b402-164f327d74ce.PNG)

![text](https://user-images.githubusercontent.com/113315434/194604679-be259ab7-e540-4e94-afa1-78264c27bb0f.PNG)

In debug mode, it can be seen that the client had sent a tweet with the text "yuzuru hanyu".

The information included response data.

![image](https://user-images.githubusercontent.com/113315434/194605470-cecb675f-0618-4b20-9286-95508a3af9d9.png)


Then I logged in to Twitter, checked my account, and the tweet was sent successfully.

![从](https://user-images.githubusercontent.com/113315434/194604960-0dd145a1-d1bc-4354-bb81-1619372a948e.PNG)

##Create a poll
On top of sending tweets, I would like to create a poll.
### Test Program
_import tweepy_

_import config_

_client=tweepy.Client(consumer_key=config.API_KEY,_
                     _consumer_secret=config.API_SECRET,_
                     _access_token=config.ACCESS_TOKEN,_
                     _access_token_secret=config.ACCESS_TOKEN_SECRET)_

_response=client.create_tweet(text="yuzuru hanyu's best performance",poll_duration_minutes=5,poll_options=['seimei','h&l','pw'])_

_print(response)_
### Result
In debug mode, it can be seen that the poll had been created successfully.

![image](https://user-images.githubusercontent.com/113315434/194605944-405de1dc-819a-470a-9c08-152ed227069d.png)

And the response data was:

![image](https://user-images.githubusercontent.com/113315434/194606506-d515a94e-7e7c-4c86-91ca-a6be63e5c87c.png)

Checking my account, there's a poll created 31 seconds ago:

![image](https://user-images.githubusercontent.com/113315434/194606804-9d61a067-501e-4c63-a45d-aabb198cc61e.png)
