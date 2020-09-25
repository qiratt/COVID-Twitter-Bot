# Copyright 2020 Tariq Scott COVID-19 tracker

import requests # allows me to send HTTP requests
import sys # provides info on how script is interacting with host system
import time # in order to schedule tweets
import tweepy # provides access to twitter API
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from lxml import html # python processing library
from datetime import datetime # so i can tweet out the current date

def build_tweet():
# current date
    #current_date = datetime.strptime()# works when i take out 'var'? interesting
    response = requests.get('https://www.worldometers.info/coronavirus/')
    # 'get' returns a value from a given key. in this case, it's the worldometers.
    # can't solely leave "doc" will get a syntax error

    doc = html.fromstring(response.content)
    # from what i can gather, it's literally "from string": 'response' and
    # (dot)content is everything that comes after the equals sign for# the given method.

    total_cases, total_deaths, total_recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')
        # XPath (or XML path language) is used to parse content from a given
        # website. so worldometers in this case. we see the content as HTML
        # though. the contents of the HTML documents are referred to as 'nodes.'
        # where XPath comes in, is it defines a path to navigate to the exact
        # HTML code that i need. so in this case, i needed everything from
        # div -> class -> maincounter -> span(body/function name) -> text
        # (the text inside of span.) worldometers named all of them the same
        # or else i would have had to write out three different scenarios.

    tweet = f'''Covid-19 Latest Updates 😷
                \n

        Total cases: {total_cases} 🤒
        Deaths: {total_deaths} ☠️
        Recovered: {total_recovered} 🤕

        #coronavirus #covid19'''

    return tweet
        # f string means 'formatted literal string' so the methods that i am
        # calling for are grouped into one body, called one by one, in
        # a single string.

        # FUTURE REFERENCE: for the bot's you make, everything at this point
        # and beyond will more than likely look identical, if not very similar.

if __name__ == '__main__':
        authorization = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        authorization.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        # creating of application program interface object
        api = tweepy.API(authorization)
        # 'API' must be CAPITALIZED when using tweepy!!

        try:
            api.verify_credentials()
            print('Authentication Successful')
        except:
            api.verify_credentials()
            print('ERROR. Authentication failed.')
            system.exit(1)

        tweet = build_tweet()
        api.update_status(tweet)
        print('Successfully tweeted')

# LEARN HOW TO PROPERLY INDENT SO YOUR CODE CAN CORRECTLY RUN
