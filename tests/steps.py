# -*- coding: utf-8 -*-
import os
import glob
import json

from freshen import *
from webtest import TestApp
from ludibrio import Stub


from twitter_poll.service import application
from twitter_poll.tweets_crawler import TweetsCrawler

URLS = {
'main':'/',
}

def get_lines():
    return scc.tweets

@Before
def before(sc):
    scc.app = TestApp(application)
    scc.tweets = []
    with Stub() as TweetsCrawler:
        from twitter_poll.tweets_crawler import TweetsCrawler
        
        TweetsCrawler.get_tweets() >> get_lines()
    
    

@Given(r"^I enter the main page $")
def given_i_enter_the_main_page_():
    scc.last_page = scc.app.get('/')

@Given(r"^I see 0 votes$")
def given_i_see_0_votes():
    mi_total = scc.last_page.lxml.cssselect('#total_agil')[0].text
    assert "0" == mi_total
    
@When(r"^I tweet '#dojovote http://ciudadanointeligente.org' as 'lfalvarez'$")
def when_i_tweet___dojovote_http___ciudadanointeligente_org__as__lfalvarez_():
    scc.tweets.append('lfalvarez\t#dojovote http://ciudadanointeligente.org')
    
@When(r"^I enter the main page $")
def when_i_enter_the_main_page_():
    scc.last_page = scc.app.get('/')

@Then(r"^I see 1 vote$")
def then_i_see_1_vote():
    mi_total = scc.last_page.lxml.cssselect('#total_agil')[0].text
    assert "1" == mi_total
