#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Tumblr Bot Starter Kit: Bot 1

## This bot posts three times, waiting 5 seconds between posts.

## If you haven't yet created credentials.py, modify credentials.template to include your own Tumblr account settings. This script will then post using your bot's account.

## Housekeeping: do not edit
import pytumblr, time
from credentials import *
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

client_info = client.info()
## To check that you are authenticated and that things are set up correctly to post, uncomment the following line and run the script. You should see some output in your terminal window. 
#print(client_info)

## Creating a text post
## What the bot will tweet --
post_list = ['Test post one', 'Test post two', 'Test post three']

## Loop through the post_list and post each item
## Uncomment lines 29-39 to run your bot: 
# for line in post_list: 
#     print('Posting to tumblr:')
#     print(line)
#     client.create_text(
#         blogname=client_info['user']['name'],
#         state='published', 
#         title='Testing',
#         body=line)
#     print('Pausing...')
#     time.sleep(5) # Pause for 5 seconds

print("All done!")


