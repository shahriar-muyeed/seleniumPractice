from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class _tshirt():

    def __init__(self, driver):
        self.driver=driver

        self.blue_filter_id="layered_id_attribute_group_14"
        self.product_class="product-container"
     

    def click_blue_filter(self):
        self.driver.find_element_by_id(self.blue_filter_id).click()

    def click_tshirt_checkout(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        men_menu = self.driver.find_element_by_class_name(self.product_class)
        actions.move_to_element(men_menu).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Add to cart']"))).click()
        
        time.sleep(10)
        
        self.driver.execute_script("document.getElementsByClassName('btn btn-default button button-medium')[0].click();");