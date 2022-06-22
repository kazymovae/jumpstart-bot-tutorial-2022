#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Tumblr Bot Starter Kit: Extra Bot 1

## This bot tweets a text file line by line, waiting a given period of time between tweets.

# Housekeeping: do not edit
import pytumblr, time
from credentials import *
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

## To check that you are authenticated and that things are set up correctly to post, uncomment the following line and run the script. You should see some output in your terminal window. 
# print(client.info())

## Reading in the text that the bot will post... 
filename = open('data/phrases_coined_by_shakespeare.txt','r') 
post_text = filename.readlines() #this creates a list: one line → one item
filename.close()

# loop through the post_text list and post to tumblr
for line in post_text[0:5]: # Will only write first 5 lines
    client.create_text(
        blogname='', #replace with your blog name
        state="published", 
        title="Phrases coined by Shakespeare...", 
        body=line)
    print(line)
    time.sleep(5) # Pause for 5 seconds

print("All done!")


## We've given you a .txt file to work with, but try this with another .txt file of your choosing! A good place to find public domain books to use is https://www.gutenberg.org/ 

## Try choosing a random line to post, rather than just the first five. (hint: you'll need to import the 'random' library)

## Tip: to quit early, press CTRL+C and wait a few seconds
