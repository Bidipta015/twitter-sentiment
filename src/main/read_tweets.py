import tweepy


def connect(config):
    client = tweepy.Client(consumer_key=config.api_key,
                           consumer_secret=config.api_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret
                           )

    return client
