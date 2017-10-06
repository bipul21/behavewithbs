from behave import given


@given('we have android app uploaded')
def step_impl(context):
    assert (context.android_app is not None)


@given('we have ios app uploaded')
def step_impl(context):
    assert (context.ios_app is not None)