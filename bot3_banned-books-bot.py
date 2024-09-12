#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Tumblr Bot Starter Kit: Bot 3

## This bot makes a post about a banned book randomly drawn from a spreadsheet of data about banned books. It posts the cover image of the book, the book title, the allged reasons it was challenged and/or banned, as well as the number of years it has spent in the top 10 most frequently challenged/banned books. 

## The data is from https://baddatapod.com/badbooks/" 

import pytumblr, csv, random
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

## Create a list of banned books 
## This line instantiates an empty list that we are going to fill in. 
banned_books =[]

## First we need to open the file and extract the data
with open('data/banned-books-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for book in reader:
        banned_books.append(book) #adds each line (or book) to that empty list we started above

## Choose a random book from that list 
chosen_book = random.choice(banned_books[2:-1]) 
print(chosen_book)

## Post to Tumblr. 
# This time, there are some blanks to fill in! Select the correct key to include in appropriate places.
client.create_photo(
    blogname=client_info['user']['name'],
    state="published",  
    source= chosen_book['Cover'],
    link= chosen_book['Link'][9:-13],
    caption= "<b><em>" + chosen_book['Title'] + '''</em></b><br><br>
    Alleged reasons this book was challenged and/or banned: <i>''' + chosen_book['Reason'] + '''</i><br><br>
    Number of years on the top 10 list of most commonly challenged/banned books = ''' + chosen_book['# of Years on Top 10 List'] + " year(s).",
    tags= ["banned books", "based on data from https://baddatapod.com/badbooks/"])

## SAMPLE OUTPUT
##
## *book photo with click-thru link*
##
## We All Fall Down
##
## Alleged reasons this book was challenged and/or banned: offensive language, sexual content
##
## Number of years on the top 10 list of most commonly challenged/banned books = 1 year(s).






