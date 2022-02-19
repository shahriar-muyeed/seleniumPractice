import time
class _mycart():

    def __init__(self, driver):
        self.driver=driver
        

        
     

    def click_tocheckout(self):
        time.sleep(5)
        self.driver.execute_script("document.getElementsByClassName('button btn btn-default standard-checkout button-medium')[0].click();");
    
    def click_tocheckout_address(self):
        time.sleep(5)
        #self.driver.execute_script("document.getElementsByClassName('button btn btn-default button-medium')[0].click();");
        self.driver.find_element_by_name("processAddress").click()
        
    def click_tocheckout_shipping(self):
        time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='cgv']").click()
        self.driver.find_element_by_name("processCarrier").click()

    def click_tocheckout_payment(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name("cheque").click()
   

    def click_tocheckout_final(self):
        time.sleep(3)
        #self.driver.find_element_by_class_name("button btn btn-default button-medium").submit()
        self.driver.find_element_by_xpath("//span[normalize-space(text())='I confirm my order']").click()
       