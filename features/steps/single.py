from behave import *
from appium import webdriver

BS_USERNAME = "bipuljain2"
BS_AUTH_TOKEN = "XKZq8VnNEJPxiQjftzsU"


@given('we have android app uploaded')
def step_impl(context):
    assert (context.android_app is not None)


@given('we have ios app uploaded')
def step_impl(context):
    assert (context.ios_app is not None)


@when('search android app with Browserstack')
def step_impl(context):
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'Google Pixel'
    desired_caps['build'] = 'Bipul Behave!!'
    desired_caps["app"] = context.android_app
    context.driver = webdriver.Remote('http://bipuljain2:XKZq8VnNEJPxiQjftzsU@hub.browserstack.com/wd/hub',
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
    driver = webdriver.Remote('http://bipuljain2:XKZq8VnNEJPxiQjftzsU@hub.browserstack.com/wd/hub',
                              desired_caps)
    context.driver = driver

    context.driver.find_element_by_id("Log In").click()
    try:
        context.driver.find_element_by_id("Email address").send_keys("hello@browserstack.com")
        context.driver.find_element_by_id("Next").click()
    except:
        context.driver.quit()

@then('we should see some search results')
def step_impl(context):
    text_elements = context.driver.find_elements_by_xpath('//XCUIElementTypeStaticText')
    assert (len(text_elements) > 0)
    for text_element in text_elements:
        print(dir(text_element))
        print(text_element.get_text())
    context.driver.quit()

@when('search android app with Browserstack')
def step_impl(context):
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'iphone 7'
    desired_caps['build'] = 'Bipul Behave!!'
    desired_caps["app"] = context.ios_app
    desired_caps["automationName"] = "XCUITest"
    driver = webdriver.Remote('http://bipuljain2:XKZq8VnNEJPxiQjftzsU@hub.browserstack.com/wd/hub',
                              desired_caps)
    context.driver = driver

    context.driver.find_element_by_id("Log In").click()
    try:
        context.driver.find_element_by_id("Email address").send_keys("hello@browserstack.com")
        context.driver.find_element_by_id("Next").click()
    except:
        context.driver.quit()



