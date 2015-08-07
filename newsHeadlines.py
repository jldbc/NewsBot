import codecs
import feedparser
import urllib2
import re
import sys
from collections import defaultdict
from random import random
with codecs.open('headlinesFile.txt', encoding = 'utf-8') as tfile:
    headlines = tfile.readlines()

#get headlines
urls = ['http://conservativetribune.com/feed/', 'http://www.americasfreedomfighters.com/feed/', 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'http://feeds.huffingtonpost.com/c/35496/f/677086/index.rss', 'http://feeds.huffingtonpost.com/c/35496/f/677055/index.rss', 'http://rss.cnn.com/rss/cnn_allpolitics.rss', 'http://thehill.com/taxonomy/term/1630/feed',  'http://thehill.com/taxonomy/term/1132/feed', 'http://thinkprogress.org/election/issue/feed/', 'http://thinkprogress.org/economy/issue/feed/', 'http://www.politico.com/rss/magazine.xml', 'http://www.theblaze.com/feed/', 'http://rightwingnews.com/feed', 'thepoliticalinsider.com/feed', 'http://radixnews.com/feed/', 'http://www.westernjournalism.com/feed/', 'http://libertyfirstnews.com/feed/', 'http://bearingarms.com/feed/', 'http://madworldnews.com/feed','http://hotair.com/feed']
for i in urls:
    feed = feedparser.parse(i)
    for j in range(len(feed.entries)):
        headlines.append(feed.entries[j].title)

titles = headlines
#print len(headlines)


#Create original headlines:

markov_map = defaultdict(lambda:defaultdict(int))
lookback = 2
#Generate map in the form word1 -> word2 -> occurences of word2 after word1
for title in titles[:-1]:
    title = title.split()
    if len(title) > lookback:
        for i in xrange(len(title)+1):
            markov_map[' '.join(title[max(0,i-lookback):i])][' '.join(title[i:i+1])] += 1

#set probabilities of word2s given word1s
for word, following in markov_map.items():
    total = float(sum(following.values()))
    for key in following:
        following[key] /= total

#Typical sampling from a categorical distribution
def sample(items):
    next_word = None
    t = 0.0
    for k, v in items:
        t += v
        if t and random() < v/t:
            next_word = k
    return next_word

sentences = []
while len(sentences) < 400:
    sentence = []
    next_word = sample(markov_map[''].items())
    while next_word != '':
        sentence.append(next_word)
        next_word = sample(markov_map[' '.join(sentence[-lookback:])].items())
    sentence = ' '.join(sentence)
    flag = True
    for title in titles: #Prune titles that are substrings of actual titles
        if sentence in title:
            flag = False
            break
    if flag:
        sentences.append(sentence)


headlinesFile = open('botLines.txt', "w")
for sentence in sentences:
	headlinesFile.write(sentence.encode('UTF-8') + '\n')






