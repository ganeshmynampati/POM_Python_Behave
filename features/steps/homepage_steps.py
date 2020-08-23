from behave import given, when, then


@given('user is on budget application home page')
def step_impl(context):
    context.home_page.ValidateHomePageHeader("Discount car rental rates and rental car deals | Budget Car Rental")

@when('user types "{LocationKey}" and selects pickup and return location as "{LocationName}"')
def step_impl(context,LocationKey,LocationName):
    context.home_page.EnterPickUpLocation(LocationKey,LocationName)

@when('pickup date as week ahead of current date')
def step_impl(context):
    context.home_page.enterPickUpDate()

@when('return date as week ahead of pickup date')
def step_impl(context):
    context.home_page.enterDropDate()

@when('clicks Select My car option to navigate to reservations page')
def step_impl(context):
    context.home_page.clickSelectMyCar()
