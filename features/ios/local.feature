
@ios @local
Feature: IoS Local Functionality

  Scenario: Show bs local page
    Given we have "ios_local" app uploaded
    when first page of app
    then we should see Up and Running

