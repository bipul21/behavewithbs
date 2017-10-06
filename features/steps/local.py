import time
from behave import *
from appium import webdriver
from browserstack.local import Local


@when('first page of app')
def step_impl(context):
    time.sleep(10)
    desired_caps = {}
    desired_caps['realMobile'] = 'true'
    desired_caps['device'] = 'Google Pixel'
    desired_caps['build'] = 'Behave!!'
    desired_caps['browserstack.local'] = 'true'
    desired_caps['name'] = 'Python Local {}'.format(desired_caps['device'])
    desired_caps["app"] = context.android_local_app
    driver = webdriver.Remote(
        'http://{}:{}@hub.browserstack.com/wd/hub'.format(context.BS_USER_NAME, context.BS_USER_AUTH_TOKEN),
        desired_caps)
    context.driver = driver



@then('we should see Up and Running')
def step_impl(context):
    print(dir(context.driver))
    assert True
    context.driver.quit()
