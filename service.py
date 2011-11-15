# -*- coding: utf-8 -*-
import os
import re
import json

import bottle
from bottle import request, redirect

bottle.TEMPLATE_PATH.insert(0,os.path.abspath(__file__))


@bottle.route('/')
@bottle.view('templates/main')
def main():
    try:
      tweets = json.loads(open('fixtures/tweets.json').read())
    except:
      tweets = []
    return dict(total = len(tweets))

    
bottle.debug(True)

application = bottle.default_app.pop()
application.catchall = False


# bottle.run(host='localhost', port=8099, reloader = True)

def main():
    reload = 'True'
    web_port = 8080
    bottle.run(app=application, host='0.0.0.0', port=web_port,reloader=reload)


if __name__ == '__main__':
    main()