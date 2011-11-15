Feature: Get current results
  In order to know people preferences
  As User
  We will see the updated number of votes per option in our page
  
  Scenario: 1 vote
    Given I enter the current results page and I see 0 options
    When I tweet '#dojovote http://epistemonikos.org' as 'dperezrada'
      and I enter the current results page
    Then I see 1 option 'http://epistemonikos.org' with 1 vote
  
  Scenario: 1 vote tweet twice
    Given I enter the current results page and I see 0 options
    When I tweet 2 times '#dojovote http://epistemonikos.org' as 'fvalverd'
      and I enter the current results page
    Then I see 1 option 'http://epistemonikos.org' with 1 vote
      
  Scenario: 2 votes with 1 option
    Given I enter the current results page and I see 0 options
    When I tweet '#dojovote http://www.zpricing.com' as 'ndujovne'
      and I tweet '#dojovote http://www.zpricing.com' as 'dperezrada'
      and I enter the current results page
    Then I see 1 option 'http://www.zpricing.com' with 2 votes