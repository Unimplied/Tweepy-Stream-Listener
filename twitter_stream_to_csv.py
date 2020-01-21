import tweepy # Twitter API
import csv # import csv for logging to file
import logging
import json

#Twitter API credentials; populate with your twitter Developer Credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Initialize API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)

# Set Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# creates stream listener class
class devTweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    # Creates file to write to, and appends tweets to it
    def on_status(self, status):
        print(status.author, "\n", status.text, "\n")
        with open('outputStream.csv', mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([status.author, "\n", status.text, "\n"])
            
    def on_error(self, status):
        logger.error(status)
        
# Main Function

def main(keywords):
    tweets_listener = devTweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    
# Insert terms to be tracked in main([]), arguments are string values held in a list
if __name__ == "__main__":
    main([])
