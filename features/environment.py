from features.browser import Browser
from features.pages.home_page import HomePage
from features.pages.reservations_page import ReservationsPage

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.reservations_page = ReservationsPage()

def after_all(context):
    context.browser.close()