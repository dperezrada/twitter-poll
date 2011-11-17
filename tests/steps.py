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

def get_tweets():
    return scc.tweets

@Before
def before(sc):
    scc.app = TestApp(application)
    scc.basepath = os.path.dirname(os.path.abspath(__file__))
    scc.tweets = []
    
    with Stub() as TweetsCrawler:
        from twitter_poll.tweets_crawler import TweetsCrawler
        tweets_crawler = TweetsCrawler()
        tweets_crawler.get_tweets() >> get_tweets()

@After
def after(sc):
    pass

def enter_to_page(page):
    scc.last_page = scc.app.get(URLS[page])
    assert_equal(200, scc.last_page.status_int)

def i_see_votes(number_votes):
    assert_equal(number_votes, scc.last_page.lxml.cssselect('#total')[0].text)

@Given(r"^I enter the (.*) page $")
def given_i_enter_the_page_(page):
    enter_to_page(page)

@Given(r"^I see ([0-9]+) votes?$")
def given_i_see_votes(number_votes):
    i_see_votes(number_votes)
  
@When(r"^I tweet '(.*)' as '(.*)'$")
def when_i_tweet(tweet, user):
    scc.tweets.append({
      "text": tweet,
      "user": user
    })
    
@When(r"^I enter the (.*) page $")
def when_i_enter_the_main_page_(page):
    enter_to_page(page)
    
@Then(r"^I see ([0-9]+) votes?$")
def then_i_see_votes(number_votes):
    i_see_votes(number_votes)