# Trash code, I'll make it better soon... Just ignore for now
# It uses too many api requests, for a free trial it just does not work.

import tweepy
import time
import keys

# ─── Set up client ────────
client = tweepy.Client(
    consumer_key= keys.consumer_key,
    consumer_secret= keys.consumer_secret,
    access_token= keys.access_token,
    access_token_secret= keys.access_token_secret,
    bearer_token= keys.bearer_token,
    wait_on_rate_limit= True
)


# ─── Set up target @ and ID ─────────────────
target_user_screen_name = "@BeckeGrr"
target_user_id = "2943818182"

# ─── Poll user_timeline and reply in real time ────────────
def monitor_and_reply(user_id: str, username: str, poll_interval: int):
    
    since_id = None
    while True:
        resp = client.get_users_tweets(
            id=user_id,
            since_id=since_id,
            max_results=5,
            exclude=["retweets", "replies"],
            tweet_fields=["created_at"]
        )
        tweets = resp.data or []
        
        tweets.reverse()
        for tweet in tweets:
            since_id = tweet.id if since_id is None else max(since_id, tweet.id)

            text = tweet.text
            print(f"🔔 New Tweet from {username}!\nID: {tweet.id} @ {tweet.created_at}:\n{text!r}")

            client.create_tweet(
                text= "super teste",
                in_reply_to_tweet_id= tweet.id,
                user_auth= True
            )
            print(f"💬 Replied to {tweet.id}")

        time.sleep(poll_interval)

if __name__ == "__main__":
    monitor_and_reply(target_user_id, target_user_screen_name, poll_interval=90)