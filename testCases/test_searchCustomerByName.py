import logging
import time
import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.loginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.customeLogger import getCustomerLogger
from utilities.read_Properties import ReadConfig

class Test_005_searchCustomerByEmial():
    global logger
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger = getCustomerLogger(logging.INFO)

    @pytest.mark.regression
    def test_searchCustomerByEmailID(self,setup):
        logger.info("*****************Test_005_SearchCustomerByName **************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        logger.info("**************************LOgin Successfull ******************")

        logger.info("**********************Starting Search by name test *******************")
        add = AddCustomer(self.driver)
        time.sleep(2)
        add.clickonCustomerMenu()
        time.sleep(2)
        add.clickOnCustomersSubMenu()
        logger.info("**********************Searching customer by name ********************")
        search = SearchCustomer(self.driver)
        search.enterFirstName("Victoria")
        search.enterLastName("Terces")
        search.clickSearch()
        time.sleep(4)
        status = search.searchCustomerByName("Victoria Terces")
        assert True == status
        logger.info("******************** TC_005_Search customer by name Finished***************")
        self.driver.close()
