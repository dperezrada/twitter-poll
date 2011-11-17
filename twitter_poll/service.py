# -*- coding: utf-8 -*-
import os
import re
import json

import bottle
from bottle import request, redirect

from twitter_poll.tweets_crawler import TweetsCrawler

#Controllers
@bottle.route('/')
@bottle.view('templates/main')
def main():
    tweets = TweetsCrawler.get_tweets()
    return dict(total = len(tweets))


#Config
bottle.TEMPLATE_PATH.insert(0,os.path.dirname(os.path.abspath(__file__)))
bottle.debug(True)
application = bottle.default_app.pop()
application.catchall = False

#To run
def main():
    reload = 'True'
    web_port = 8080
    bottle.run(app=application, host='0.0.0.0', port=web_port,reloader=reload)


if __name__ == '__main__':
    main()