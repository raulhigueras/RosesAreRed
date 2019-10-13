import tweepy
import time
from bot import GEN

file = open("twittertokens.txt", "r")
tokens = [file.readline().rstrip(), file.readline().rstrip(), file.readline().rstrip(), file.readline().rstrip()]
auth = tweepy.OAuthHandler(tokens[0], tokens[1])
auth.set_access_token(tokens[2], tokens[3])


api = tweepy.API(auth)

maxId = 1
while(True):
    mentions = api.mentions_timeline(since_id=maxId)
    for tweet in mentions:
        if tweet.in_reply_to_status_id:
            status = api.get_status(tweet.in_reply_to_status_id)
            text = status.text
            res = GEN.generateText(6, text[-1])
            api.update_status("Roses are red, \n" + res + ". https://twitter.com/" + status.user.screen_name + "/status/" + str(status.id))

    maxId = mentions[0].id if len(mentions) > 0 else maxId
    time.sleep(30)
