import time
class _signout():

    def __init__(self, driver):
        self.driver=driver

        
     

    def click_signout(self):
        self.driver.find_element_by_xpath('//*[@title="Log me out"]').click()