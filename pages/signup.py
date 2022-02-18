class _signup():

    def __init__(self, driver):
        self.driver=driver

        self.email_textBox_id="email_create"
        self.submit_create_id="SubmitCreate"

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textBox_id).clear()
        self.driver.find_element_by_id(self.email_textBox_id).send_keys(email)
    
    def click_create_account(self):
        self.driver.find_element_by_id(self.submit_create_id).click()