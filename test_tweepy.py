import tweepy

consumer_key = "gZ63HdXjanJEKx3CvILfhQzQ5"
consumer_secret = "LN7MhwTMqnTb2Mn3kUAZAcJvql6hLUw9c0yD8JxJO3X2Rp0Ne2"
access_token = "26843310-CqgjMKrQ2B4sNybS6E0jcrnN6aSliohLrbha49nrM"
access_token_secret = "D4rS4X47XAmLJwQ8QlemErrGaiNqT6O9QTToZingzvQra"

def get_replies_1(tweet_id):
    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the replies to the tweet
    replies = api.search_tweets(q='to:SPECIFIC_TWEET_USER', since_id=tweet_id, tweet_mode='extended')

    return replies


def get_replies_2(tweet_id):
    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweet = api.get_status(tweet_id)

    # Get the replies to the tweet
    replies = api.search_tweets(q='to:{}'.format(tweet.user.screen_name), since_id=tweet_id, tweet_mode='extended')

    return replies


def get_replies_3(tweet_id):
    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweet = api.get_status(tweet_id)

    # Get the replies to the tweet
    replies = api.search(q='@{} exclude:retweets'.format(tweet.user.screen_name), since_id=tweet_id, tweet_mode='extended')
    return replies

# Specify the tweet ID for which you want to retrieve replies
tweet_id = "1679759294428790785"

# Get the replies for the specified tweet
replies = get_replies_1(tweet_id)

# Iterate over the replies and print them
for reply in replies:
    print(reply.full_text)
