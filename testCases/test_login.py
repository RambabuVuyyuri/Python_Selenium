from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.read_Properties import ReadConfig
from utilities.customeLogger import getCustomerLogger
import logging
import pytest

class Test_001_Login:
    global logger
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger = getCustomerLogger(logging.DEBUG)


    @pytest.mark.regresion
    def test_homePageTitle(self,setup):
        logger.info("*********************Test_001_Login****************")

        logger.info("********************** Verifyig Home Page Titile***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            logger.info("*********************** HOme page titile test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False
            logger.info("************************** Home page title test faile and captured SS ************")
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        logger.info("************************* Verifying Login Test ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        actual_title = self.driver.title
        lp.clickLogout()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            logger.info("********************** Login Home page passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
            logger.info("*************************** LOgin test failed and captured SS: ****************")
