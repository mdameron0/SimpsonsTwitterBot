#********************************
# Time is poorly implemented, I hotfixed this in the active bot, however, I never changed the "master" file.
# Linking does not work, why? because Twitter was refusing the links. Not sure why, didnt have time to figure it out, so I just let it go.
# point is, note that the links dont work, but it creates the correct string.
# Tweepy is the API I am using, link to docs/site: https://github.com/tweepy/tweepy
# The program ran on about 2Mb of ram, so I never went threw to optimize.
#********************************
import tweepy
import datetime
import time

#We're going to just open all the txt files with Read/write super privilage because I'm lazy.

#opens the episodeList
EpisodeList = open ("EpisodeListEdited.txt", "r+")

#opens the log file and asigns it the variable logfile
LogFile = open("BotLog.txt", "r+")

#opens the Link List.
LinkList = open("LinkListEdited.txt", "r+")

#api Auth
auth = tweepy.OAuthHandler("Api authentication here","API authentication here")

#Access Auth
auth.set_access_token("account/access auth here","Account/access auth here")

#passes auth to create a logged in API wrapper
api = tweepy.API(auth)


#basic message to be appended to every tweet
#old message: currently airing on #fxx : 
basicMessage = "Starting on #EverySimpsonsEver:"

#same as above but for the link tweet
basicLink = "Wiki link to currently airing episode: "

#puts all the episode lines into one variable list.
episodeData = EpisodeList.readlines()

#same as above but with the links
linkData = LinkList.readlines()


#close all the things!
EpisodeList.close()
LinkList.close()


def sendTweet(episodeLine):
	#make all the strings that will be put into the tweets
	episodeString = basicMessage + " " + episodeData[episodeLine]
	#the basic base URL that will then append the link.
	linkString = basicLink + "simpsons.wikia.com" + linkData[episodeLine]
	try:
		#TODO:
		#add link tweet
		api.update_status(episodeString)
		LogFile.write("tweeted " + episodeString + " at "  + time.localtime().tm_hour + time.localtime().tm_min + "\n")
		time.sleep(60)
		api.update_status(linkString)
		LogFile.write("tweeted " + linkString + " at "  + time.localtime().tm_hour + time.localtime().tm_min + "\n")
	except:
		#threw an error everytime because of the link tweet.
		LogFile.write("Something went wrong when tweeting \n")
		pass


def main ():
	run = True
	#change to the starting episodes line. = currentepisode - 1
	currentLine = 0 #change to number of line in text file at time of deployment
	#hommerazi
	while run:
		if CheckTime() == True:
			checkMovie()
			currentLine+=1
			sendTweet(currentLine)
			print "tweeting, sleeping"
			time.sleep(200)
		#this is the last episode to air
		if currentLine == 553:
			run = False
			logfile.close()
		print "sleep"
		time.sleep(90)
		

#Fxx ran the movie Friday at 6
def checkMovie():
	now = datetime.datetime.now()
	#checks for 6 PM on friday.
	#technically you should check the month etc but since it was expected to 
	if (now.hour == 18 and now.day == 29):
		#update twitter for movie.
		api.update_status("Sit back and relax, the simpsons movie is starting. #notUnderTheDome brb changing batteries #EverySimpsonsEver")
		#sleeps for 3 hours. The ammount of skill here is unreal.
		time.sleep(10800)
	else:
		pass


#checks the time to see if drops on the half hour. 
#returns true if it's time to update.
def CheckTime():
	now = datetime.datetime.now()

	if (now.minute >= 30 and now.minute <= 32) or (now.minute >= 0 and now.minute <= 2):
		return True

	else:
		return False

main()