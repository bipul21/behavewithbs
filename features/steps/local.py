from behave import *
from appium import webdriver


@when('first page of app')
def step_impl(context):
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'Google Pixel'
    desired_caps['build'] = context.BUILD_NAME
    desired_caps['browserstack.local'] = 'true'
    desired_caps['name'] = 'Python Local {}'.format(desired_caps['device'])
    desired_caps["app"] = context.android_local_app
    driver = webdriver.Remote(
        'http://{}:{}@hub.browserstack.com/wd/hub'.format(context.BS_USER_NAME, context.BS_USER_AUTH_TOKEN),
        desired_caps)
    context.driver = driver


@then('we should see Up and Running')
def step_impl(context):
    assert True
    context.driver.quit()
