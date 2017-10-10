from behave import *
from appium import webdriver
from constants import *


@given('we have "{device_type}" app uploaded')
def step_impl(context, device_type):
    if device_type == "android":
        assert (context.android_app is not None)
    elif device_type == "ios":
        assert (context.ios_app is not None)


@when('search "{device_type}" app with Browserstack')
def step_impl(context, device_type):
    desired_caps = {'realMobile': 'true', 'build': context.BUILD_NAME}

    if device_type == 'android':
        desired_caps['device'] = ANDROID_DEVICE_TYPE
        desired_caps["app"] = context.android_app
    elif device_type == "ios":
        desired_caps['device'] = IOS_DEVICE_TYPE
        desired_caps["app"] = context.ios_app
        desired_caps["automationName"] = "XCUITest"

    desired_caps['name'] = 'Basic {}'.format(desired_caps['device'])
    context.desired_caps = desired_caps
    context.driver = webdriver.Remote(
        'http://{}:{}@hub.browserstack.com/wd/hub'.format(context.BS_USER_NAME, context.BS_USER_AUTH_TOKEN),
        desired_caps)
    context.driver.find_element_by_id("Search Wikipedia").send_keys("BrowserStack")


@then('we should see some search results')
def step_impl(context):
    text_elements = context.driver.find_elements_by_class_name("android.widget.TextView")
    assert (len(text_elements) > 0)
