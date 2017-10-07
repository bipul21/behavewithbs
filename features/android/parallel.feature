@android @parallel
Feature: BS Parallel Sessions Functionality

  Scenario: Just run a plain app
    Given we have "android" app uploaded
    when just open the app
    then we should see the app


