import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.customeLogger import getCustomerLogger
from utilities.read_Properties import  ReadConfig
from utilities import XLUtils
import logging

class Test_002_login_ddt():
    global logger
    baseurl = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = getCustomerLogger(logging.INFO)

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        logger.info("***********************Test_02_login_DDT***************************")
        logger.info("*********************** Verifying login test ddt ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(file=self.path,sheetname='Sheet1')
        print("the number of row count is :",self.rows)
        lst_status =[]
        for i in range(2,self.rows+1):
            print("iterating rown number ",i)
            user = XLUtils.readData(self.path,'Sheet1',i,1)
            print("username:",user)
            password = XLUtils.readData(self.path,'Sheet1',i,2)
            print("password:", password)
            exp = XLUtils.readData(self.path,'Sheet1',i,3)
            print("exp:", exp)
            self.lp.setUserName(user)
            self.lp.setPassword(password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_text = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_text==exp_title:
                if exp=='Pass':
                    logger.info("*******Passed*********")
                    self.lp.clickLogout()
                    lst_status.append('Pass')
                elif exp == 'Fail':
                    logger.info("********** Failed ********")
                    self.lp.clickLogout()
                    lst_status.append('Fail')
            elif actual_text != exp_title:
                if exp == 'Pass':
                    logger.info("************ failed***********")
                    lst_status.append('Fail')
                elif exp == 'Fail':
                    logger.info("**************** Passed **********")
                    lst_status.append('Pass')

        print("LIst value after appended",lst_status)
        if 'Fail' not in lst_status:
            logger.info("****************Login DDT test Passed*****************")
            self.driver.close()
            assert True
        else:
            logger.info("**************** Failed *************")
            self.driver.close()
            assert False

        logger.info("***************** End of the DDT test case****************")
        logger.info("********************** End of the Test_002_login_DDt test ****************")