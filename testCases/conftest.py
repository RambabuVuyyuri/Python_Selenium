import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/Ram/Desktop/nopecommerceApp/Lib/chromedriver.exe")
        print("launched chrome browser")
    elif browser.lower() == "firefox":
        driver = webdriver.Chrome(executable_path="C:/Users/Ram/Desktop/nopecommerceApp/Lib/chromedriver.exe")
        print("launched firefox browser")
    else:
        driver = webdriver.Chrome(executable_path="C:/Users/Ram/Desktop/nopecommerceApp/Lib/chromedriver.exe")
        print("launched default chrome browser")

    return driver
################### Pytest Html Report###############3

#It is hook for adding Environment info into Html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ramu'

# It is hook for delete/modify Environment info into HTML report

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)
    metadata.pop('Packages',None)


def pytest_addoption(parser):  # this will get the values from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
