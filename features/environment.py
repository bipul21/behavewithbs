from browserstack.local import Local
import json

BS_CONFIG = json.load(open('bs_config.json'))

BS_USER_NAME = BS_CONFIG['BS_USER_NAME']
BS_USER_AUTH_TOKEN = BS_CONFIG['BS_USER_AUTH_TOKEN']


def before_feature(context, feature):
    if "local" in feature.tags:
        bs_local = Local()
        bs_local_args = {"key": context.BS_USER_AUTH_TOKEN, "forcelocal": "true"}
        context.bs_local = bs_local
        context.bs_local.start(**bs_local_args)


def after_feature(context, feature):
    if "local" in feature.tags:
        context.bs_local.stop()


def before_all(context):
    context.android_app = BS_CONFIG['ANDROID_APP']
    context.ios_app = BS_CONFIG['IOS_APP']
    context.android_local_app = BS_CONFIG['ANDROID_LOCAL_APP']
    context.ios_local_app = BS_CONFIG["IOS_LOCAL_APP"]
    context.BUILD_NAME = BS_CONFIG["BUILD_NAME"]
    context.BS_USER_NAME = BS_USER_NAME
    context.BS_USER_AUTH_TOKEN = BS_USER_AUTH_TOKEN