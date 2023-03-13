from selenium import webdriver
from selenium.webdriver.common.by import By
from POMProject.Locators.Locator import pageLocator


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_xpath= pageLocator.dropdown_xpath
        self.logout_link_xpath= pageLocator.logout_link_xpath
        self.myinfo_xpath= pageLocator.myinfo_xpath

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    def click_myinfo(self):
        self.driver.find_element(By.XPATH,self.myinfo_xpath).click()