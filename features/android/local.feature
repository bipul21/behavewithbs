
@android @local
Feature: Android Local Functionality

  Scenario: Show bs local page
    Given we have "android_local" app uploaded
    when first page of app
    then we should see Up and Running

