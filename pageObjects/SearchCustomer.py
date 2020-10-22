class SearchCustomer():

    # Add customer page elements
    txtEmail_id = "SearchEmail"
    txtfirstname_id ="SearchFirstName"
    txtlastname_id ="SearchLastName"
    btnsearch_id="search-customers"

    tblsearchResults_xpath ="//table[@role='grid']"
    table_xpath ="//table[@id='customers-grid']"
    tablerows_xpath ="//table[@id='customers-grid']//tbody/tr"
    tablecolumns_xpath ="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def enterEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def enterFirstName(self,fname):
        self.driver.find_element_by_id(self.txtfirstname_id).clear()
        self.driver.find_element_by_id(self.txtfirstname_id).send_keys(fname)

    def enterLastName(self,lname):
        self.driver.find_element_by_id(self.txtlastname_id).clear()
        self.driver.find_element_by_id(self.txtlastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnsearch_id).click()

    def getNoRows(self):
        return len(self.driver.find_elements_by_xpath(self.tablerows_xpath))

    def getNoColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tablecolumns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for x in range(1,self.getNoRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(x)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        flag = False
        for x in range(1,self.getNoRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            searchname = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(x)+"]/td[3]").text
            if searchname == name:
                flag = True
                break
        return flag







