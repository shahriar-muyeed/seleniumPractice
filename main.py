import time
import unittest
import warnings
import random, string
from pages.home_page import home_page
from pages.signup import _signup
from pages.signin import _signin
from pages.userHome import _userhome
from pages.tshirt import _tshirt
from pages.mycart import _mycart
from pages.casualDressess import _casuladressess
from pages.authentication import authentication
from selenium import webdriver
from pages.signout import _signout


#------------------------initialize driver---------------------------------
class webtester(unittest.TestCase):


    


    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning) 
        warnings.filterwarnings("ignore", category=DeprecationWarning) 
        #self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php") 

    
    

    def test_signup1(self):
        driver=self.driver
        signout=_signout(driver)

        random_email1='user+' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '@gmail.com'
        random_email2='user+' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '@gmail.com'
        password="123456789"

        def signup(driver,email,customer_firstName,customer_lastname,customer_email,password,firstname,lastname,company,address1,address2,city,state,postcode,country,extra,phone,mobile_phone,alias):

            homepage = home_page(driver)
            homepage.click_signin()

            signupp = _signup(driver)
            signupp.enter_email(email)
            signupp.click_create_account()

            authenticationn = authentication(driver)
            authenticationn.click_title()
            authenticationn.enter_customer_firstname(customer_firstName)
            authenticationn.enter_customer_lastname(customer_lastname)
            authenticationn.enter_email(customer_email)
            authenticationn.enter_password(password)
            authenticationn.enter_firstname(firstname)
            authenticationn.enter_lastname(lastname)
            authenticationn.enter_company(company)
            authenticationn.enter_address1(address1)
            authenticationn.enter_address2(address2)
            authenticationn.enter_city(city)
            authenticationn.enter_state(state)
            authenticationn.enter_postalcode(postcode)
            authenticationn.enter_country(country)
            authenticationn.enter_extra(extra)
            authenticationn.enter_phone(phone)
            authenticationn.enter_mobile_phone(mobile_phone)
            authenticationn.enter_alias(alias)
            authenticationn.click_create_account()


        def testCycle(random_email,password):
            signin=_signin(self.driver)
            signin.enter_email(random_email)
            signin.enter_password(password)
            signin.click_signin()

            userhome=_userhome(self.driver)
            userhome.click_casual_dresses()

            casuladressess=_casuladressess(self.driver)
            casuladressess.click_dress()
            casuladressess.click_tshirt()

            tshirt=_tshirt(self.driver)
            tshirt.click_blue_filter()
            tshirt.click_tshirt_checkout()

            cart=_mycart(self.driver)
            cart.click_tocheckout()
            cart.click_tocheckout_address()
            cart.click_tocheckout_shipping()
            cart.click_tocheckout_payment()
            cart.click_tocheckout_final()
            signout=_signout(self.driver)
            signout.click_signout()
        
        signup(driver,random_email1,"muyeed","shahriar",random_email1,password,"muyeed","shahriar","BS_23","mohakhali","dhaka","Dhaka","dhaka","12345","Bangladesh","bla bla","123456789","987456321","gg")
        signout.click_signout()
        signup(driver,random_email2,"muyeed","shahriar",random_email2,password,"muyeed","shahriar","BS_23","mohakhali","dhaka","Dhaka","dhaka","12345","Bangladesh","bla bla","123456789","987456321","gg")
        signout.click_signout()

        testCycle(random_email1,password)
        testCycle(random_email2,password)


    
    @classmethod
    def tearDown(self):
        time.sleep(3)                                         
        self.driver.close() 



if __name__== '__main__':
    unittest.main()
                            