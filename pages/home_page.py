class home_page():

    def __init__(self, driver):
        self.driver=driver

        self.signin_name="login"
   
    def click_signin(self):
        self.driver.find_element_by_class_name(self.signin_name).click()
    

           