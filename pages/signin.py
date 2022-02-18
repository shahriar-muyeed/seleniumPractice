import time
class _signin():

    def __init__(self, driver):
        self.driver=driver

        
        self.email_textBox_id="email"
        self.password_textBox_id="passwd"
        self.submit_login__id="SubmitLogin"

    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_textBox_id).clear()
        self.driver.find_element_by_id(self.email_textBox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textBox_id).clear()
        self.driver.find_element_by_id(self.password_textBox_id).send_keys(password)

    def click_signin(self):
        time.sleep(5)
        self.driver.find_element_by_id(self.submit_login__id).click()


