from selenium import webdriver
from selenium.webdriver.common.by import By
from POMProject.Locators.Locator import pageLocator

class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_name= pageLocator.username_textbox_name
        self.password_textbox_name= pageLocator.password_textbox_name
        self.login_btn_xpath= pageLocator.login_btn_xpath
        self.invalidUsernameXpath= pageLocator.invalidUsernameXpath
        self.emptyUsernameXpath= pageLocator.emptyUsernameXpath
        self.emptyPasswordXpath= pageLocator.emptyPasswordXpath
        self.emptyUsernamePasswordXpath= pageLocator.emptyUsernamePasswordXpath

    def enter_username(self,username):
        self.driver.find_element(By.NAME,pageLocator.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def press_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def check_invalid_username_message(self):
        msg=self.driver.find_element(By.XPATH,self.invalidUsernameXpath).text
        return msg

    def check_empty_username_message(self):
        msg=self.driver.find_element(By.XPATH,self.emptyUsernameXpath).text
        return msg

    def check_empty_password_message(self):
        msg=self.driver.find_element(By.XPATH,self.emptyPasswordXpath).text
        return msg

    def check_empty_username_password_message(self):
        msg=self.driver.find_element(By.XPATH,self.emptyUsernamePasswordXpath).text
        return msg
