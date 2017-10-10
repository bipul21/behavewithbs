@ios @parallel
Feature: BS Parallel Sessions Functionality on iOS

  Scenario: Just run a plain app
    Given we have "ios" app uploaded
    when just open the app
    then we should see the app
