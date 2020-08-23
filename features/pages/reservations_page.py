from selenium.webdriver.common.by import By
from features.browser import Browser
from features.utilities.test_base import TestBase

class ReservationPageLocator(object):

    TravelTimeLabel = (By.XPATH, "//*[@class='location step2']")
    PickUpLabel = (By.XPATH, "//a[text()[contains(.,'Pick-Up')]]")
    PickUpLocLabel = (By.XPATH, "//a[text()[contains(.,'Pick-Up')]]/following::div[1]")
    PickUpTimeLabel = (By.XPATH, "//a[text()[contains(.,'Pick-Up')]]/following::div[@class='day-time-info'][1]")
    ReturnLabel = (By.XPATH, "//a[text()[contains(.,'Return')]]")
    ReturnLocLabel = (By.XPATH, "//a[text()[contains(.,'Return')]]/following::div[1]")
    ReturnTimeLabel = (By.XPATH, "//a[text()[contains(.,'Return')]]/following::div[@class='day-time-info'][1]")
    AllVehiclesDropDown = (By.XPATH, "//a[@id='res-vehicles-filter-by-vehicle-type']")
    SuvGroupOption = (By.XPATH, "//div[contains(@class,'vehListRule')]/span[contains(text(),'SUVs')]/parent::div")
    SortByDropDown = (By.XPATH, "//a[@id='res-vehicles-sort']")
    LowToHighPriceOption = (By.XPATH, "//ul[@class='dropdown-menu']/descendant::a[text()[contains(.,'Low to High')]]")
    ViewVehicleInformation = (By.XPATH, "//*[@class='step2dtl']/descendant::a[text()='View Vehicle Information']")
    CloseVehicleInformation = (By.XPATH, "//a[@id='res-vehicles-details' and text()='Close Vehicle Information']")
    FourDoorVehicle = (By.XPATH, "//span[text()[contains(.,'4 Doors')]]")
    FiveSeatsVehicle = (By.XPATH, "//span[@class='four-seats-feat' and text()[contains(.,'5 seats')]]")
    SuvGroup = (By.XPATH, "//*[@class='step2dtl']/descendant::h3[@ng-bind='car.carGroup']")
    SuvName = (By.XPATH, "//*[@class='step2dtl']/descendant::p[contains(@class,'similar-car')]")
    TransMode = (By.XPATH, "//*[@class='step2dtl']/descendant::p[@ng-bind='car.automaticCaption']")
    BasePrice = (By.XPATH, "//*[@class='step2dtl']/descendant::price/span")
    PayNowOption = (By.XPATH, "//a[text()='Pay Now']")
    RentalSummary = (By.XPATH, "//section[contains(@class,'rental-summary')]")
    ConfirmPickupLoc = (By.XPATH, "//*[contains(@class,'source')]/descendant::div[@class='location-info']")
    ConfirmPickupTime = (By.XPATH, "//*[contains(@class,'source')]/descendant::div[@class='day-time-info']")
    ConfirmReturnLoc = (By.XPATH, "//*[contains(@class,'destination')]/descendant::div[@class='location-info']")
    ConfirmReturnTime = (By.XPATH, "//*[contains(@class,'destination')]/descendant::div[@class='day-time-info']")
    FinalVehicleInfo = (By.XPATH, "//div[@ng-show='mode']/descendant::div[@class='vehicle-name']/parent::div")
    ConfirmSUVGroup = (By.XPATH, "//div[@ng-show='mode']/descendant::div[@class='vehicle-name']")
    ConfirmSUVName = (By.XPATH, "//*[@ng-show='mode']/descendant::div[@class='vehicle-info']/span")
    ConfirmTransMode = (By.XPATH, "//*[@ng-show='mode']/descendant::div[contains(@ng-bind,'Transmission')]")
    FinalBaseRate = (By.XPATH, "//div[@class='optBaseRateRow']/span/span[2]")
    ConfirmFeeTaxes = (By.XPATH, "//div[@class='optTaxesRow']/span/span[2]")
    EstimatedTotal = (By.XPATH, "//div[contains(@class,'optEstimatedTotalRow')]/span/span[2]")

class ReservationsPage(Browser, TestBase):

    GroupName=""
    VehicleName=""
    ModeOfTrans=""
    BaseRate=""

    def validateReservationsPageHeaders(self):
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.TravelTimeLabel))
        self.verifyPageTitle("Reservations | Budget Car Rental")
        assert self.driver.find_element(*ReservationPageLocator.PickUpLabel).is_displayed()
        assert self.driver.find_element(*ReservationPageLocator.ReturnLabel).is_displayed()

    def validatePickUpReturnDetails(self):
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.PickUpLocLabel))
        assert "Austin Bergstrom Intl Airport" in self.driver.find_element(*ReservationPageLocator.PickUpLocLabel).text
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.PickUpTimeLabel))
        reformattedDt = TestBase.reformatFutureWeekDt(1)
        assert reformattedDt in self.driver.find_element(*ReservationPageLocator.PickUpTimeLabel).text
        assert "Austin Bergstrom Intl Airport" in self.driver.find_element(*ReservationPageLocator.ReturnLocLabel).text
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.ReturnTimeLabel))
        reformattedDt2 = TestBase.reformatFutureWeekDt(2)
        assert reformattedDt2 in self.driver.find_element(*ReservationPageLocator.ReturnTimeLabel).text

    def selectSUVType(self):
        self.jseclick(self.driver.find_element(*ReservationPageLocator.AllVehiclesDropDown))
        self.jseclick(self.driver.find_element(*ReservationPageLocator.SuvGroupOption))

    def selectSUVPrice(self):
        self.jseclick(self.driver.find_element(*ReservationPageLocator.SortByDropDown))
        self.jseclick(self.driver.find_element(*ReservationPageLocator.LowToHighPriceOption))

    def validateAndSelectSUV(self, door, seat):
        i=-1
        for info in self.driver.find_elements(*ReservationPageLocator.ViewVehicleInformation):
            i=i+1
            self.jseclick(info)
            if(
                    door in self.driver.find_elements(*ReservationPageLocator.FourDoorVehicle)[i].text and
                    seat in self.driver.find_elements(*ReservationPageLocator.FiveSeatsVehicle)[i].text
            ):
                print("Success")
                global GroupName, VehicleName, ModeOfTrans, BaseRate
                GroupName =self.driver.find_elements(*ReservationPageLocator.SuvGroup)[i].text
                print(GroupName)
                VehicleName = self.driver.find_elements(*ReservationPageLocator.SuvName)[i].text
                print(VehicleName)
                ModeOfTrans = self.driver.find_elements(*ReservationPageLocator.TransMode)[i].text
                print(ModeOfTrans)
                BaseRate = self.driver.find_elements(*ReservationPageLocator.BasePrice)[i].text
                print(BaseRate)
                self.jseclick(self.driver.find_elements(*ReservationPageLocator.CloseVehicleInformation)[i])
                self.waitForElementToBeVisible(self.driver.find_elements(*ReservationPageLocator.PayNowOption)[i])
                self.jseclick(self.driver.find_elements(*ReservationPageLocator.PayNowOption)[i])
                break
            break


    def confirmHireDuration(self):
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.RentalSummary))

        assert "Austin Bergstrom Intl Airport" in self.driver.find_element(*ReservationPageLocator.ConfirmPickupLoc).text
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.ConfirmPickupTime))
        FinalPickUpDt=TestBase.reformatFutureWeekDt(1)
        assert FinalPickUpDt in self.driver.find_element(
            *ReservationPageLocator.ConfirmPickupTime).text

        assert "Austin Bergstrom Intl Airport" in self.driver.find_element(
            *ReservationPageLocator.ConfirmReturnLoc).text
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.ConfirmReturnTime))
        FinalReturnDt = TestBase.reformatFutureWeekDt(2)
        assert FinalReturnDt in self.driver.find_element(
            *ReservationPageLocator.ConfirmReturnTime).text

    def confirmSUVDetails(self):
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.FinalVehicleInfo))
        assert GroupName in self.driver.find_element(*ReservationPageLocator.ConfirmSUVGroup).text
        assert VehicleName in self.driver.find_element(*ReservationPageLocator.ConfirmSUVName).text
        assert ModeOfTrans in  self.driver.find_element(*ReservationPageLocator.ConfirmTransMode).text
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.FinalBaseRate))
        self.jseclick(self.driver.find_element(*ReservationPageLocator.ConfirmSUVGroup))
        self.waitForElementToBeVisible(self.driver.find_element(*ReservationPageLocator.FinalBaseRate))
        assert BaseRate in self.driver.find_element(*ReservationPageLocator.FinalBaseRate).text

    def calculatePrepaidEstimates(self):
        EstBasePrice=round(float(self.driver.find_element(*ReservationPageLocator.FinalBaseRate).text),2)
        print(EstBasePrice)
        EstFeeTaxes=round(float(self.driver.find_element(*ReservationPageLocator.ConfirmFeeTaxes).text),2)
        print(EstFeeTaxes)
        ExpectedPrepaidEst=str(round(EstBasePrice+EstFeeTaxes,2))
        print(ExpectedPrepaidEst)
        ActualPrepaidEst=self.driver.find_element(*ReservationPageLocator.EstimatedTotal).text
        print(ActualPrepaidEst)
        assert ExpectedPrepaidEst==ActualPrepaidEst
        print("SuccessFinal")
