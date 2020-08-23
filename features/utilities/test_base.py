from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import datetime

class TestBase:
    def clearElement(self,ele):
        self.waitForElementToBeVisible(ele)
        self.scrollIntoView(ele)
        ele.clear()

    def eleClick(self,ele):
        self.waitForElementToBeClickable(ele)
        ele.click()

    def jseclick(self, ele):
        self.waitForElementToBeVisible(ele)
        self.scrollIntoView(ele)
        self.driver.execute_script("arguments[0].click();", ele)

    def setText(self, ele, text):
        self.waitForElementToBeVisible(ele)
        ele.send_keys(text)

    def getText(self,ele):
        self.waitForElementToBeVisible(ele)
        self.scrollIntoView(ele)
        return ele.text

    def waitForElementToBeVisible(self, webelement):
        wait = WebDriverWait(self.driver, 60)
        wait.until(expected_conditions.visibility_of(webelement))

    def verifyPageTitle(self,expectedTitle):
        match=False
        actualTitle=self.driver.title
        if actualTitle==expectedTitle:
            match=True
        return match

    def actionsClick(self, ele):
        actions=ActionChains(self.driver)
        actions.move_to_element(ele).click(ele).perform()

    @staticmethod
    def selectDropdownByText(webelement, text):
        select = Select(webelement)
        select.select_by_visible_text(text)

    def waitForElementToBeClickable(self, ele):
        wait = WebDriverWait(self.driver, 60)
        wait.until(expected_conditions.element_to_be_clickable(ele))

    @staticmethod
    def getFutureDateByWeek(num):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(weeks=num)
        next_week_date=datetime.date.strftime(next_week, "%m/%d/%Y")
        return next_week_date

    def scrollIntoView(self, ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    @staticmethod
    def reformatFutureWeekDt(num):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(weeks=num)
        return datetime.date.strftime(next_week, "%a, %b %d")
