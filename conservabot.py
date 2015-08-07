import time
import random
import tweepy

auth = tweepy.OAuthHandler('<Consumer Key>', '<Consumer Secret>')
auth.set_access_token('<Access Key>', '<Access Secret>')
api = tweepy.API(auth)
handle = "breaking_gop"

with open('botLines.txt') as tfile:
        tweetsource = tfile.readlines()


#tweet every half hour
while True:
	try:
		rand = random.randint(1, len(tweetsource)) 
		tweet = tweetsource[rand] 
		api.update_status(status = tweet[:140])
		print ("tweeted" + tweet)
	except:
		print "error with tweet. trying a new one later."
	time.sleep(60*30)
   