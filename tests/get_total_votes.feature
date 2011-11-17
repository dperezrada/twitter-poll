Feature: Get total votes
  In order to know how many people has voted
  As User
  We will see the updated number of votes in our page
  
  Scenario: 0 votes
    Given I enter the main page 
      And I see 0 votes
    When I tweet '#dojovote http://ciudadanointeligente.org' as 'lfalvarez'
      And I enter the main page 
    Then I see 1 vote