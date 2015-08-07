# NewsBot
A Twitter bot that writes its own news headlines based on a training set of politically biased right-wing sources and HackerNews headlines.
I released this into the wild for a short time. You can see the results at twitter.com/breaking_gop


Botlines.txt contains a list of hackernews post titles
headlinesFile.txt is empty - this is where the newly created headlines will be stored
newsHeadlines.py parses the political sites' headlines and then writes its own using Markov chains 
conservabot.py is the twitter bot itself - tweets from the list of generated headlines every half hour
