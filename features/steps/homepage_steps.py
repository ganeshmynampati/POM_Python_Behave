from behave import step

@step('user is on budget application home page')
def step_impl(context):
    context.home_page.ValidateHomePageHeader("Discount car rental rates and rental car deals | Budget Car Rental")

@step('user types "{LocationKey}" and selects pickup and return location as "{LocationName}"')
def step_impl(context,LocationKey,LocationName):
    context.home_page.EnterPickUpLocation(LocationKey,LocationName)

@step('pickup date as week ahead of current date')
def step_impl(context):
    context.home_page.enterPickUpDate()

@step('return date as week ahead of pickup date')
def step_impl(context):
    context.home_page.enterDropDate()

@step('clicks Select My car option to navigate to reservations page')
def step_impl(context):
    context.home_page.clickSelectMyCar()

@step(u'chooses lowest price SUV with "4" doors and "5" seats and click pay now option')
def step_impl(context):
    pass



@step(u'user validates base rate, fees and taxes and estimated prepaid total succesfully')
def step_impl(context):
    pass

