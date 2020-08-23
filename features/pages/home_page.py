from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from features.browser import Browser
from features.pages.reservations_page import ReservationsPage
from utilities.test_base import TestBase

class HomePageLocator(object):
    BudgetHeader = (By.XPATH, "//*[@class='navbar-brand']")
    PickupLocation = (By.XPATH, "//*[@id='from']/preceding::input[@id='PicLoc_value']")
    PickupDropDownOptions = (By.XPATH, "//*[@id='from']/preceding::input[@id='PicLoc_value']/"
                                       "following::div[@class='angucomplete-results'][1]/div[1]")
    PickupDropDownValues = (By.XPATH, "//*[contains(@ng-repeat,'suggestions')]/"
                                      "descendant::span[contains(@class,'result-name')]")
    OptionToSelect = (By.XPATH, "//*[contains(@ng-repeat,'suggestions')]/"
                                "descendant::div[contains(@ng-click,'selectResult(')]")
    PickupDate = (By.XPATH, "//*[@id='from']")
    PickupTime = (By.XPATH, "//*[@id='from']/following::select[1]")
    DropLocation = (By.XPATH, "//*[@id='to']/preceding::input[@id='DropLoc_value']")
    DropDate = (By.XPATH, "//*[@id='to']")
    DropTime = (By.XPATH, "//*[@id='from']/following::select[2]")
    SelectCar = (By.XPATH, "//button[@id='res-home-select-car']")


class HomePage(Browser, TestBase):

    def ValidateHomePageHeader(self, header):
        TestBase.verifyPageTitle(header)
        assert self.driver.find_element(*HomePageLocator.BudgetHeader).is_displayed()


    def EnterPickUpLocation(self, keyword, location):
        TestBase.setText(self.driver.find_element(*HomePageLocator.PickupLocation),keyword)
        DropDownValues = self.driver.find_element(*HomePageLocator.PickupDropDownValues)
        TestBase.waitForElementToBeClickable(DropDownValues)
        i=-1
        for option in self.driver.find_elements(*HomePageLocator.PickupDropDownValues):
            i=i+1
            if option.text in location:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_elements(*HomePageLocator.PickupDropDownValues)[i]).\
                    click().perform(self.driver.find_elements(*HomePageLocator.OptionToSelect)[i])
                break
        TestBase.scrollIntoView(self.driver.find_element(*HomePageLocator.PickupDate))

    def enterPickUpDate(self):
        TestBase.clearElement(self.driver.find_element(*HomePageLocator.PickupDate))
        TestBase.scrollIntoView(self.driver.find_element(*HomePageLocator.PickupDate))
        TestBase.setText(self.driver.find_element(*HomePageLocator.PickupDate), TestBase.getFutureDateByWeek(1))

    def enterDropDate(self):
        TestBase.clearElement(self.driver.find_element(*HomePageLocator.DropDate))
        TestBase.scrollIntoView(self.driver.find_element(*HomePageLocator.DropDate))
        TestBase.setText(self.driver.find_element(*HomePageLocator.PickupDate), TestBase.getFutureDateByWeek(2))

    def clickSelectMyCar(self):
        TestBase.jseclick(self.driver.find_element(*HomePageLocator.SelectCar))
        return ReservationsPage()
