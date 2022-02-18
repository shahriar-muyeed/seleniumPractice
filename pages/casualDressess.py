from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class _casuladressess():
    
    def __init__(self, driver):
        self.driver=driver
        main_page = self.driver.current_window_handle
        self.product_class="product-container"

    def click_dress(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        men_menu = self.driver.find_element_by_class_name(self.product_class)
        actions.move_to_element(men_menu).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Add to cart']"))).click()
        
    def click_continue_shopping(self):
        
        
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@title='Continue shopping']").click()