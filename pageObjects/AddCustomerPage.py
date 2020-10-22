from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class AddCustomer():

    # Creating static variables of webelements
    lnkcustomer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkcustomers_menuitem_xpath ="//span[@class='menu-item-title'][contains(text(),'Customers')][1]"
    btnaddnew_xpath ="//a[@class='btn bg-blue']"
    txtemail_xpath ="//input[@id='Email']"
    txtpassword_xpath="//input[@id='Password']"
    txtcustomerrole_xpath ="//label[contains(text(),'Customer roles')]/following::div[@role='listbox']"
    lstitemAdmistr_xpath ="//li[contains(text(),'Administrators')]"
    lstitemguest_xpath ="//li[contains(text(),'Guests')]"
    lstitemsregistered_xpath ="//li[contains(text(),'Registered')]"
    lstitemsVendor_xpath ="//li[contains(text(),'Vendors')]"
    drpvendors_xpath ="//select[@id='VendorId']"
    rdomale_xpath ="Gender_Male"
    rdofemale_xpath ="Gender_Female"
    txtfirstname_xpath ="//input[@id='FirstName']"
    txtlastname_xpath ="//input[@id='LastName']"
    txtdob_xpath ="//input[@id='DateOfBirth']"
    txtcompanyname_xpath ="//input[@id='Company']"
    txtadmincomment_xpath ="//textarea[@id='AdminComment']"
    btnsave_xpath ="//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomer_menu_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomers_menuitem_xpath).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.btnaddnew_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element_by_xpath(self.txtemail_xpath).send_keys(email)

    def enerPassword(self,password):
        self.driver.find_element_by_xpath(self.txtpassword_xpath).send_keys(password)

    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerrole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            element = self.driver.find_element_by_xpath(self.lstitemsregistered_xpath)
        elif role == 'Administrators':
            element = self.driver.find_element_by_xpath(self.lstitemAdmistr_xpath)
        elif role =='Guests':
            # here user can eiter be registered or guest not both
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            element = self.driver.find_element_by_xpath(self.lstitemguest_xpath)
        elif role == 'Vendors':
            element = self.driver.find_element_by_xpath(self.lstitemsVendor_xpath)

        else:
            element = self.driver.find_element_by_xpath(self.lstitemguest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",element)

    def setManagerofVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpvendors_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdomale_xpath).click
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdofemale_xpath).click()
        else:
            self.driver.find_element_by_id(self.rdomale_xpath).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtfirstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtlastname_xpath).send_keys(lname)

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtdob_xpath).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element_by_xpath(self.txtcompanyname_xpath).send_keys(cname)

    def setAdmincontent(self,content):
        self.driver.find_element_by_xpath(self.txtadmincomment_xpath).send_keys(content)

    def clickSaveButton(self):
        self.driver.find_element_by_xpath(self.btnsave_xpath).click()
