import random
import time
import pytest
import string
import logging
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.read_Properties import ReadConfig
from utilities.customeLogger import getCustomerLogger

class Test_003_AddCustomer():
    global logger
    baseurl =ReadConfig.getApplicationUrl()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger = getCustomerLogger(logging.INFO)

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        logger.info("************Test_003_AddCustomer************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        lp =LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        logger.info("**************** LOgin SuccessFull **************")

        logger.info("******************** Started Add customer test *************")

        add= AddCustomer(self.driver)
        time.sleep(2)
        add.clickonCustomerMenu()
        time.sleep(2)
        add.clickOnCustomersSubMenu()
        add.clickAddNew()
        logger.info("***************** Started adding Customer Info***************")


        email = random_generator()+'@gamail.com'
        add.enterEmail(email)
        add.enerPassword("test1234")
        add.setCustomerRole('Guests')
        add.setManagerofVendor('Vendor 2')
        add.setGender('Male')
        add.setFirstName('Rambabu')
        add.setLastName('Vuyyuri')
        add.setDOB('7/08/1996')
        add.setCompanyName('TechM')
        add.setAdmincontent('This is practice testing')
        add.clickSaveButton()

        logger.info("********************Saving Customer Info***************")

        logger.info("***********************Add customer Validation Started************")
        msg = self.driver.find_element_by_tag_name('body').text

        #print(msg)
        if 'customer has been added successfully.' in msg:
            assert True == True
            logger.info("***************Add Customer test passed ***************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\addCustomer.png")
            logger.error("***************Add customer test failed**************")
            assert True == False

        self.driver.close()
        logger.info("***************Ending Home page title text*************")



def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))