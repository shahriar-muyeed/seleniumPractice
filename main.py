from time import time
from pages.home_page import home_page
from pages.signup import _signup
from pages.signin import _signin
from pages.authentication import authentication
from selenium import webdriver
import random, string
from pages.signout import _signout


#os.environ['PATH'] += r"/home/ghost/Muyeed/BS23/venv/"#get webdriver URL
driver = webdriver.Chrome() #initialize driver

driver.get("http://automationpractice.com/index.php") #go to the URL

def signup(email,customer_firstName,customer_lastname,customer_email,password,firstname,lastname,company,address1,address2,city,state,postcode,country,extra,phone,mobile_phone,alias):

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
    

random_email1='user+' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '@gmail.com'
random_email2='user+' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '@gmail.com'
password="123456789"
signup(random_email1,"muyeed","shahriar",random_email1,password,"muyeed","shahriar","BS_23","mohakhali","dhaka","Dhaka","dhaka","12345","Bangladesh","bla bla","123456789","987456321","gg")


signout=_signout(driver)
signout.click_signout()


signup(random_email2,"muyeed","shahriar",random_email2,password,"muyeed","shahriar","BS_23","mohakhali","dhaka","Dhaka","dhaka","12345","Bangladesh","bla bla","123456789","987456321","gg")
signout.click_signout()

# driver.get("http://automationpractice.com/index.php")
# homepage = home_page(driver)
# homepage.click_signin()
# signin=_signin(driver)
# signin.enter_email(random_email1)
# signin.enter_password(password)
# signin.click_signin()



# time.sleep(3)                                         #wait for 3 seconds
# driver.close()                                        #close driver