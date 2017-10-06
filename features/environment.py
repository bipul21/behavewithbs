from browserstack.local import Local
import json

BS_CONFIG = json.load(open('bs_config.json'))

BS_USER_NAME = BS_CONFIG['BS_USER_NAME']
BS_USER_AUTH_TOKEN = BS_CONFIG['BS_USER_AUTH_TOKEN']

def before_all(context):
    context.android_app = "bs://e5c03d2a951df442d3860c8db7f824d981cab901"
    context.ios_app = "bs://96635476b0724d8e7f1f1895e01356dced80f407"
    context.android_local_app = "bs://a14b125653ad4942cfa456fb4e355bcc797a1611"
    context.ios_local_app = "bs://38aecd3b9ded0a5413ce3986a36935540dc542f6"
    context.BS_USER_NAME = BS_USER_NAME
    context.BS_USER_AUTH_TOKEN = BS_USER_AUTH_TOKEN
    bs_local = Local()
    bs_local_args = {"key": context.BS_USER_AUTH_TOKEN, "forcelocal": "true"}
    context.bs_local = bs_local
    context.bs_local.start(**bs_local_args)

def after_all(context):
    # pass
    # context.driver.quit()
    context.bs_local.stop()