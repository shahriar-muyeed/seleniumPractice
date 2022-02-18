import time

class authentication():

    def __init__(self, driver):
        self.driver=driver

        #self.title_xpath=
        self.customer_firstname_id="customer_firstname"
        self.customer_lastname_id="customer_lastname"
        self.customer_email_id="email"
        self.password_id="passwd"
        self.firstname_id="firstname"
        self.lastname_id="lastname"
        self.company_id="company"
        self.address1_id="address1"
        self.address2_id="address2"
        self.city_id="city"
        self.state_id="id_state"
        self.postcode_id="postcode"
        self.country_id="id_country"
        self.extrainfo_id="other"
        self.phone_id="phone"
        self.phone_mobile_id="phone_mobile"
        self.alias_id="alias"

        self.submit_account_id="submitAccount"
        



    def click_title(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='id_gender1']").click()
       

    def enter_customer_firstname(self, customer_firstname):
        self.driver.find_element_by_id(self.customer_firstname_id).clear()
        self.driver.find_element_by_id(self.customer_firstname_id).send_keys(customer_firstname)
    
    def enter_customer_lastname(self, customer_lastname):
        self.driver.find_element_by_id(self.customer_lastname_id).clear()
        self.driver.find_element_by_id(self.customer_lastname_id).send_keys(customer_lastname)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.customer_email_id).clear()
        self.driver.find_element_by_id(self.customer_email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.firstname_id).clear()
        self.driver.find_element_by_id(self.firstname_id).send_keys(firstname)
    
    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_id).clear()
        self.driver.find_element_by_id(self.lastname_id).send_keys(lastname)

    def enter_company(self, company):
        self.driver.find_element_by_id(self.company_id).clear()
        self.driver.find_element_by_id(self.company_id).send_keys(company)

    def enter_address1(self, address1):
        self.driver.find_element_by_id(self.address1_id).clear()
        self.driver.find_element_by_id(self.address1_id).send_keys(address1)

    def enter_address2(self, address2):
        self.driver.find_element_by_id(self.address2_id).clear()
        self.driver.find_element_by_id(self.address2_id).send_keys(address2)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.city_id).clear()
        self.driver.find_element_by_id(self.city_id).send_keys(city)

    def enter_state(self, state):
        #self.driver.find_element_by_id(self.state_id).clear()
        self.driver.find_element_by_id(self.state_id).send_keys(state)

    def enter_postalcode(self, postalcode):
        self.driver.find_element_by_id(self.postcode_id).clear()
        self.driver.find_element_by_id(self.postcode_id).send_keys(postalcode)

    def enter_country(self, country):
        #self.driver.find_element_by_id(self.country_id).clear()
        self.driver.find_element_by_id(self.country_id).send_keys(country)

    def enter_extra(self, extra):
        self.driver.find_element_by_id(self.extrainfo_id).clear()
        self.driver.find_element_by_id(self.extrainfo_id).send_keys(extra)

    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.phone_id).clear()
        self.driver.find_element_by_id(self.phone_id).send_keys(phone)

    def enter_mobile_phone(self, mobile_phone):
        self.driver.find_element_by_id(self.phone_mobile_id).clear()
        self.driver.find_element_by_id(self.phone_mobile_id).send_keys(mobile_phone)

    def enter_alias(self, alias):
        self.driver.find_element_by_id(self.alias_id).clear()
        self.driver.find_element_by_id(self.alias_id).send_keys(alias)
    
    def click_create_account(self):
        time.sleep(10)
        self.driver.find_element_by_id(self.submit_account_id).submit()