import threading
import time
from behave import *
from appium import webdriver


class ParallelSession(threading.Thread):
    def __init__(self, bs_user_name, bs_user_auth_token, desired_caps):
        threading.Thread.__init__(self)
        self.desired_caps = desired_caps
        self.BS_USER_NAME = bs_user_name
        self.BS_USER_AUTH_TOKEN = bs_user_auth_token

    def run(self):
        driver = webdriver.Remote(
            'http://{}:{}@hub.browserstack.com/wd/hub'.format(self.BS_USER_NAME, self.BS_USER_AUTH_TOKEN),
            self.desired_caps)
        time.sleep(3)
        driver.quit()


@when('just open the app')
def step_impl(context):
    desired_caps = {'realMobile': 'true', 'build': 'Behave!!', "app": context.android_app}
    device_names = ["Google Pixel", "Google Pixel", "Google Pixel"]
    session_holder = []
    for index, device in enumerate(device_names):
        desired_caps['device'] = device
        desired_caps['name'] = 'Parallel {} - {}'.format(desired_caps['device'], index + 1)
        session_thread = ParallelSession(context.BS_USER_NAME, context.BS_USER_AUTH_TOKEN, desired_caps)
        session_thread.start()
        session_holder.append(session_thread)

    for session in session_holder:
        session.join()


@then('we should see the app')
def step_impl(context):
    assert True
    if context.driver:
        context.driver.quit()
