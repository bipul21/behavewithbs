
@android
Feature: Wikipedia Search Functionality on Android

  Scenario: can find search results
    Given we have android app uploaded
    when search android app with Browserstack
    then we should see some search results



