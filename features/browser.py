from selenium import webdriver

class Browser(object):
    driver = webdriver.Chrome(executable_path="./features/drivers/chromedriver.exe")
    driver.get("https://www.budget.com/en/home")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
