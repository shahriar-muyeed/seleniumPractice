from pages.home_page import home_page
from pages.signup import _signup
from pages.authentication import authentication
from selenium import webdriver
import time



#os.environ['PATH'] += r"/home/ghost/Muyeed/BS23/venv/"#get webdriver URL
driver = webdriver.Chrome() #initialize driver

driver.get("http://automationpractice.com/index.php") #go to the URL

homepage = home_page(driver)
homepage.click_signin()

signupp = _signup(driver)
signupp.enter_email("nu@gmail.com")
signupp.click_create_account()

authenticationn = authentication(driver)
authenticationn.click_title()
authenticationn.enter_customer_firstname("jhon")
authenticationn.enter_customer_lastname("shahriar")
authenticationn.enter_email("nu@gmail.com")
authenticationn.enter_password("123456789")
authenticationn.enter_firstname("customer1")
authenticationn.enter_lastname("rahman")
authenticationn.enter_company("BS")
authenticationn.enter_address1("dhaka")
authenticationn.enter_address2("mohakhali")
authenticationn.enter_city("dhaka")
authenticationn.enter_state("dhaka")
authenticationn.enter_postalcode("1234")
authenticationn.enter_country("Bangladesh")
authenticationn.enter_extra("jhon doe")
authenticationn.enter_phone("0123478958")
authenticationn.enter_mobile_phone("01957013351")
authenticationn.enter_alias("bla bla")
authenticationn.click_create_account()






# time.sleep(3)                                         #wait for 3 seconds
# driver.close()                                        #close driver