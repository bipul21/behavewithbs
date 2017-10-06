import os, json
from browserstack.local import Local

bs_local = None


def before_all(context):
    context.android_app = "bs://e5c03d2a951df442d3860c8db7f824d981cab901"
    context.ios_app = "bs://96635476b0724d8e7f1f1895e01356dced80f407"
    context.android_local_app = "bs://a14b125653ad4942cfa456fb4e355bcc797a1611"
    context.ios_local_app = "bs://38aecd3b9ded0a5413ce3986a36935540dc542f6"


def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = {"key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true"}
    bs_local.start(**bs_local_args)


def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()
