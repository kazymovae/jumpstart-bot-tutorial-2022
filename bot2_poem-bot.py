#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Tumblr Bot Starter Kit: Bot 2

## This bot generates one variant of a poem using a mad-libs technique, replacing 3 words in the original with 3 randomly-chosen words from 3 word lists.

## Original poem: This Is Just To Say by William Carlos Williams
## https://poets.org/poem/just-say

import pytumblr, time, json
from random import randint
from credentials import *
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

client_info = client.info()
## To check that you are authenticated and that things are set up correctly to post, uncomment the following line and run the script. You should see some output in your terminal window. 
# print(client_info)


## First, we need to read in our word lists from the data folder so that we can use them. The word lists are in the json format. 
## fruits
with open('data/fruits.json') as fruit_data:
   fruit_response = json.load(fruit_data)

## adjectives
with open('data/adjectives.json') as adjectives_data:
   adjectives_response = json.load(adjectives_data)

# colors
with open('data/colors.json') as colors_data:
   colors_response = json.load(colors_data)

## Extract a Python-readable list from each response
fruits = fruit_response['fruits']
adjectives = adjectives_response['adjs']
colors = colors_response['colors']
    
## Pick random numbers
## (randint(0, len(xxx)-1) means choose random number between 0 and the length of the word list named xxx) 
fruit_num = randint(0, len(fruits)-1) 
adjectives_num = randint(0, len(adjectives)-1)
color_num = randint(0, len(colors)-1)

## Choose random items from each list using those random numbers
fruit_chosen = fruits[fruit_num].lower()
color_chosen = colors[color_num]['color'].lower()
adjective_chosen = adjectives[adjectives_num].lower()

## Fill in the blanks of the poem with the randomly chosen items
## <br> is an html tag that means insert a line break
## \ at end of line just splits the line in the code, so that the code can be read more easily 

poem = 'This is just to say<br>\
I have eaten<br>\
the {0}s <br>\
that were in <br>\
the icebox <br><br>\
and which <br>\
you were probably <br>\
saving <br>\
for breakfast <br><br>\
Forgive me <br>\
they were delicious <br>\
so {1} <br>\
and so {2}' \
   .format(fruit_chosen, color_chosen, adjective_chosen)

## Post to Tumblr
client.create_text(
   blogname=client_info['user']['name'],
   state="published", 
   title="This is just to say...", 
   body=poem, 
   tags=["Original poem: This Is Just To Say by William Carlos Williams"])

print(poem)

## SAMPLE OUTPUT

## I have eaten
## the kumquats
## that were in
## the icebox
##
## and which
## you were probably
## saving
## for breakfast
##
## Forgive me
## they were delicious
## so unmellow yellow
## and so waterproof