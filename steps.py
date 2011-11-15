# -*- coding: utf-8 -*-
import os
import glob
import json

from freshen import *
from webtest import TestApp


from service import application

URLS = {
'main':'/',
}

@Before
def before(sc):
    scc.app = TestApp(application)

@After
def after(sc):
    files = glob.glob('fixtures/*.json')
    for f in files:
        os.remove(f)

@Given(r"^I enter the (.*) page $")
def given_i_enter_the_page_(page):
    scc.last_page = scc.app.get(URLS[page])
    assert_equal(200, scc.last_page.status_int)

@Given(r"^I see 0 votes$")
def given_i_see_0_votes():
    assert_equal('0',scc.last_page.lxml.cssselect('#total')[0].text)
  
@When(r"^I tweet '#dojovote http://ciudadanointeligente.org' as 'lfalvarez'$")
def when_i_tweet___dojovote_http___ciudadanointeligente_org__as__lfalvarez_():
    open('fixtures/tweets.json', 'w').write('''[{
      "text": "#dojovote http://ciudadanointeligente.org",
      "user": "lfalvarez"
    }]''')
    
@When(r"^I enter the (.*) page $")
def when_i_enter_the_main_page_(page):
    scc.last_page = scc.app.get(URLS[page])
    assert_equal(200, scc.last_page.status_int)
    
@Then(r"^I see 1 vote$")
def then_i_see_1_vote():
    assert_equal('1',scc.last_page.lxml.cssselect('#total')[0].text)