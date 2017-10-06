#@android_parallel
#Feature: Wikipedia Search Functionality on Android
#
#  Scenario: can find search results
#    Given we have android app uploaded
#    when search android app with Browserstack
#    then we should see some search results
#
#
## Created by bipul at 06/10/17
#Feature: #Enter feature name here
#  # Enter feature description here
#
#  Scenario: # Enter scenario name here
#    # Enter steps here

@android @local
Feature: Android Local Functionality

  Scenario: Show bs local page
    Given we have android app uploaded
    when open bs-local.com:45691
    then we should see "Up and Running"

