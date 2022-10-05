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
        login_link = self.driver.find_element ('xpath', '/html/body/header/div/nav[1]/div/a[1]')
        login_link.click()
      
        # Locate login boxes
        
        user_field = self.driver.find_element('xpath','/html/body/main/section/div/div/form/div[1]/div[1]/label/input')
        last_name_field = self.driver.find_element ('xpath','/html/body/main/section/div/div/form/div[1]/div[2]/label/input')
        pass_field = self.driver.find_element ('xpath','/html/body/main/section/div/div/form/div[1]/div[3]/label/input')
        login_button = self.driver.find_element ('xpath','/html/body/main/section/div/div/form/div[2]/div/button')
        
        # Get login credentials
        
        user = input ("AAdvantage# or Username: " )
        last_name= input ("Last Name: ")
        password = getpass ("Password: ")
        
        user_field.send_keys(user)
        sleep(2)
        last_name_field.send_keys(last_name)
        sleep(2)
        pass_field.send_keys(password)
        sleep(4)
        login_button.click()

bot = CardOfferBot()
bot.open_simplymiles()
bot.simplymiles_login()