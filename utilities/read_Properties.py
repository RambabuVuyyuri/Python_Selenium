import configparser
"""
this .ini - initializing file used as configuration file and we can read data from this file
this is available under "Configparser" module and have to creare object for RawConfigParser() class
and we have read method to read whichaccepts file path as perameter and loads data
"""
config = configparser.RawConfigParser()
config.read('C:/Users/Ram/Desktop/nopecommerceApp/Configurations/config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','baseurl')
        print(url)
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getApplicationpassword():
        password = config.get("common info", "password")
        return password
