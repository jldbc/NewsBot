# NewsBot
A Twitter bot that writes its own news headlines based on a training set of politically biased sources and HackerNews headlines.
I released this into the wild for a short time. You can see the results at twitter.com/breaking_gop


<br>Botlines.txt contains a list of hackernews post titles</br>
<br>headlinesFile.txt is empty - this is where the newly created headlines will be stored</br>
<br>newsHeadlines.py parses the political sites' headlines and then writes its own using Markov chains </br>
<br>conservabot.py is the twitter bot itself - tweets from the list of generated headlines every half hour</br>
