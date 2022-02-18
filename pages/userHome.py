from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class _userhome():

    def __init__(self, driver):
        self.driver=driver

        self.dresses_class="sf-with-ul"

    def click_casual_dresses(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        men_menu = self.driver.find_element_by_class_name(self.dresses_class)
        actions.move_to_element(men_menu).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Casual Dresses']"))).click()
