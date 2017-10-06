from behave import *
from appium import webdriver

BS_USERNAME = "bipuljain2"
BS_AUTH_TOKEN = "XKZq8VnNEJPxiQjftzsU"



@when('search android app with Browserstack')
def step_impl(context):
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'Google Pixel'
    desired_caps['build'] = 'Behave'
    desired_caps["app"] = context.android_app
    context.desired_caps = desired_caps
    context.driver = webdriver.Remote(
        'http://{}:{}@hub.browserstack.com/wd/hub'.format(context.BS_USER_NAME, context.BS_USER_AUTH_TOKEN),
        desired_caps)
    context.driver.find_element_by_id("Search Wikipedia").send_keys("BrowserStack")


@when('search ios app with Browserstack')
def step_impl(context):
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'iphone 7'
    desired_caps['build'] = 'Bipul Behave!!'
    desired_caps["app"] = context.ios_app
    desired_caps["automationName"] = "XCUITest"
    context.desired_caps = desired_caps



@then('we should see some search results')
def step_impl(context):
    text_elements = context.driver.find_elements_by_xpath('//XCUIElementTypeStaticText')
    assert (len(text_elements) > 0)
    # context.driver.quit()

