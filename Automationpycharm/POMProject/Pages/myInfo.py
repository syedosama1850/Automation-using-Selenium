from selenium.webdriver.common.by import By
import os
import sys
from POMProject.Locators.Locator import pageLocator

class MyInfo():
    def __init__(self, driver):
        self.driver = driver
        self.add_btn_xpath = pageLocator.add_btn_xpath
        self.browse_btn_xpath = pageLocator.browse_btn_xpath
        self.save_btn_Xpath = pageLocator.save_btn_Xpath
        self.largefilemessage_xpath= pageLocator.largefilemessage_xpath
        self.emptyfilemessage_xpath = pageLocator.emptyfilemessage_xpath
        self.maleradio_btn_xpath= pageLocator.maleradio_btn_xpath
        self.radio_save_btn_xpath= pageLocator.radio_save_btn_xpath
        self.smoker_radiobtn_xpath= pageLocator.radio_save_btn_xpath
        self.maritalstatus_dropdown_xpath= pageLocator.maritalstatus_dropdown_xpath
        self.marriedstatus_btn_xpath= pageLocator.marriedstatus_btn_xpath

    def click_add(self):
        self.driver.find_element(By.XPATH,self.add_btn_xpath).click()

    def click_browse(self):
        file=self.driver.find_element(By.XPATH,self.browse_btn_xpath)
        file.send_keys('D:/Coding/Automationpycharm/POMProject/Files/dslifecycle.png')

    def click_browse_largefile(self):
        file=self.driver.find_element(By.XPATH,self.browse_btn_xpath)
        file.send_keys('D:/Coding/Automationpycharm/POMProject/Files/DSPresentation.pptx')

    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_btn_Xpath).click()

    def check_largefile_message(self):
        msg=self.driver.find_element(By.XPATH,self.largefilemessage_xpath).text
        return msg

    def check_emptyfile_message(self):
        msg=self.driver.find_element(By.XPATH,self.emptyfilemessage_xpath).text
        return msg

    def click_maleradio_btn(self):
        self.driver.find_element(By.XPATH,self.maleradio_btn_xpath).click()

    def click_radio_save_btn(self):
        self.driver.find_element(By.XPATH,self.radio_save_btn_xpath).click()

    def click_smoker_radio_btn(self):
        self.driver.find_element(By.XPATH, self.smoker_radiobtn_xpath).click()

    def click_marital_dropdown(self):
        self.driver.find_element(By.XPATH,self.maritalstatus_dropdown_xpath).click()
        self.driver.find_element(By.XPATH,self.marriedstatus_btn_xpath).click()

