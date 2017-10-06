
@ios
Feature: Wikipedia Search Functionality on IOS

  Scenario: can find search results
    Given we have ios app uploaded
    when search ios app with Browserstack
    then we should see some search results

