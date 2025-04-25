import keys
import tweepy

user = tweepy.Client(
    consumer_key= keys.consumer_key,
    consumer_secret= keys.consumer_secret,
    access_token= keys.access_token,
    access_token_secret= keys.access_token_secret,
    bearer_token= keys.bearer_token,
    wait_on_rate_limit= True
)

post_text = "atumalakakakaka"
try: 
    user.create_tweet(
        text= post_text,
        in_reply_to_tweet_id= "1915430008144683124"
    )
    print("Tweet created successfully!")
except:
    print("Failed to post.")