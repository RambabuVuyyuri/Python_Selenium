import logging
import time
import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.loginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.customeLogger import getCustomerLogger
from utilities.read_Properties import ReadConfig

class Test_004_searchCustomerByEmial():
    global logger
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger = getCustomerLogger(logging.INFO)

    @pytest.mark.regression
    def test_searchCustomerByEmailID(self,setup):
        logger.info("*****************Test_004_SearchCustomerByEmail **************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize.window()

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        logger.info("**************************LOgin Successfull ******************")

        logger.info("**********************Starting Search by Email test *******************")
        add = AddCustomer(self.driver)
        add.clickonCustomerMenu()
        add.clickOnCustomersSubMenu()
        logger.info("**********************Searching customer by email id ********************")
        search = SearchCustomer(self.driver)
        search.enterEmail("victoria_victoria@nopCommerce.com")
        search.clickSearch()
        time.sleep(4)
        status = search.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        logger.info("******************** TC_004_Search customer by email id Finished***************")
        self.driver.close()
