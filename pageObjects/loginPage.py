from selenium import webdriver
import time


'''
This is login page object contains webelements of the login page and web actions methods
this page object will be created in test case and class accepts drivers as parameter
'''

class LoginPage:
    txtbox_username_id ="Email"
    txtbox_password_id ="//input[@name='Password']"
    button_login_xpath ="//input[@class='button-1 login-button']"
    link_logout_linktext ="Logout"

    def __init__(self,driver):
        self.driver =driver


    def setUserName(self,username):
        self.driver.find_element_by_id(self.txtbox_username_id).clear()
        self.driver.find_element_by_id(self.txtbox_username_id).send_keys(username)
        print("entered username")
    def setPassword(self,password):
        time.sleep(2)

        self.driver.find_element_by_xpath(self.txtbox_password_id).clear()
        self.driver.find_element_by_xpath(self.txtbox_password_id).send_keys(password)
        print("entered pasword")

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
        print("clicked login button")

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        print("clicked logout button")