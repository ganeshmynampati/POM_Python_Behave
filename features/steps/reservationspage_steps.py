from behave import given, when, then

@when('chooses lowest price SUV with "{DoorNo}" doors and "{SeatNo}" seats and click pay now option')
def step_impl(context,DoorNo,SeatNo):
    context.reservations_page.validateReservationsPageHeaders()
    context.reservations_page.validatePickUpReturnDetails()
    context.reservations_page.selectSUVType()
    context.reservations_page.selectSUVPrice()
    context.reservations_page.validateAndSelectSUV(DoorNo,SeatNo)


@then('user validates base rate, fees and taxes and estimated prepaid total succesfully')
def step_impl(context):
    context.reservations_page.confirmHireDuration()
    context.reservations_page.confirmSUVDetails()
    context.reservations_page.calculatePrepaidEstimates()
