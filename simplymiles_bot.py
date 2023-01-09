from selenium import webdriver
from time import sleep
from getpass import getpass


class CardOfferBot():
    
    # Open an intance of Chrome & navigate to SimplyMiles Webpage

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_simplymiles(self):
        self.driver.get('https://www.simplymiles.com/')

        sleep(1)

    # Click login from bannner (top right)

    def simplymiles_login(self):
        login_link = self.driver.find_element(
            'xpath', '/html/body/header/div/nav[1]/div/a[1]')
        login_link.click()
        
        sleep(1)
    
    def simplymiles_loginid_locate(self):
        
        # Get login credentials

        user = input("AAdvantage# or Username: ")
        password = getpass("Password: ")

        # Locate login boxes

        user_field = self.driver.find_element(
            'xpath', '//*[@id="username-text"]')
        pass_field = self.driver.find_element(
            'xpath', '//*[@id="password-password"]')
        login_button = self.driver.find_element(
            'xpath', '//*[@id="button_login"]')

        user_field.send_keys(user)
        sleep(2)
        pass_field.send_keys(password)
        sleep(4)
        login_button.click()

    def simplymiles_offerselect(self):
        pass

bot = CardOfferBot()
bot.open_simplymiles()
bot.simplymiles_login()
bot.simplymiles_loginid_locate()
# bot.simplymiles_offerselect()