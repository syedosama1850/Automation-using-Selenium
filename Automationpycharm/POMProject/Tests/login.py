from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
import time
import unittest
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.myInfo import MyInfo
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver_manager.chrome import ChromeDriverManager
# import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class LoginTest(unittest.TestCase):
    browser = 'edge'

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        # cls.driver = webdriver.Chrome(service=service)
        # if LoginTest.browser == 'Chrome':
        #     # path = "C:\Users\usqgl\OneDrive\Desktop\Automationpycharm\Automationpycharm\POMProject\Files\Drivers\chromedriver.exe"
        #     cls.driver = webdriver.Chrome(executable_path=r"C:\Users\usqgl\OneDrive\Desktop\Automationpycharm\Automationpycharm\POMProject\Files\Drivers\chromedriver.exe")
        #     # cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #     # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # elif LoginTest.browser == 'edge':
        #     path = 'C://Users//Lenovo//Downloads//edgedriver_win64//msedgedriver.exe'
        #     cls.driver = webdriver.Edge(executable_path=path)

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.press_login_btn()

        homepage = HomePage(driver)
        homepage.click_dropdown()
        time.sleep(3)
        homepage.click_logout()
        time.sleep(3)

    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username('Admin1')
        login.enter_password('admin123')
        time.sleep(3)
        login.press_login_btn()
        time.sleep(3)
        message = login.check_invalid_username_message()
        self.assertEqual(message, 'Invalid credentials')
        time.sleep(3)

    def test_03_login_invalid_password(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username('Admin')
        login.enter_password('admin1234')
        time.sleep(3)
        login.press_login_btn()
        time.sleep(3)
        message = login.check_invalid_username_message()
        self.assertEqual(message, 'Invalid credentials')
        time.sleep(3)

    def test_04_login_empty_username(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username(' ')
        login.enter_password('admin123')
        time.sleep(3)
        login.press_login_btn()
        time.sleep(3)
        message = login.check_empty_username_message()
        self.assertEqual(message, 'Required')
        time.sleep(3)

    def test_05_login_empty_password(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username('Admin')
        login.enter_password(' ')
        time.sleep(3)
        login.press_login_btn()
        time.sleep(3)
        message = login.check_empty_password_message()
        self.assertEqual(message, 'Required')
        time.sleep(3)

    def test_06_login_empty_username_password(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username(' ')
        login.enter_password(' ')
        time.sleep(3)
        login.press_login_btn()
        time.sleep(3)
        message = login.check_empty_username_password_message()
        self.assertEqual(message, 'Required')
        time.sleep(3)

    def test_07_uploadfile_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.press_login_btn()

        homepage = HomePage(driver)
        homepage.click_myinfo()
        time.sleep(3)

        myinfo = MyInfo(driver)
        myinfo.click_add()
        time.sleep(2)
        myinfo.click_browse()
        time.sleep(10)
        myinfo.click_save()
        time.sleep(5)
        homepage.click_dropdown()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(1)

    def test_08_uploadfile_invalid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        login.enter_username('Admin')
        time.sleep(2)
        login.enter_password('admin123')
        time.sleep(2)
        login.press_login_btn()

        homepage = HomePage(driver)
        time.sleep(2)
        homepage.click_myinfo()
        time.sleep(2)

        myinfo = MyInfo(driver)
        myinfo.click_add()
        time.sleep(2)
        myinfo.click_browse_largefile()
        time.sleep(10)
        message = myinfo.check_largefile_message()
        self.assertEqual(message,'Attachment Size Exceeded')
        # myinfo.click_save()
        time.sleep(6)
        homepage.click_dropdown()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(1)

    # def test_09_uploadfile_empty(self):
    #     driver = self.driver
    #     driver.get('https://opensource-demo.orangehrmlive.com')
    #     login = LoginPage(driver)
    #     login.enter_username('Admin')
    #     login.enter_password('admin123')
    #     login.press_login_btn()
    #
    #     homepage = HomePage(driver)
    #     homepage.click_myinfo()
    #     time.sleep(3)
    #
    #     myinfo = MyInfo(driver)
    #     myinfo.click_add()
    #     time.sleep(2)
    #     # myinfo.click_browse_largefile()
    #     # time.sleep(3)
    #     myinfo.click_save()
    #     message = myinfo.check_emptyfile_message()
    #     self.assertEqual(message,'Required')
    #     # myinfo.click_save()
    #     time.sleep(2)

    def test_10_click_maleradio_btn(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        login.enter_username('Admin')
        time.sleep(2)
        login.enter_password('admin123')
        time.sleep(2)
        login.press_login_btn()

        homepage = HomePage(driver)
        time.sleep(2)
        homepage.click_myinfo()
        time.sleep(3)

        myinfo = MyInfo(driver)
        myinfo.click_maleradio_btn()
        time.sleep(5)
        myinfo.click_smoker_radio_btn()
        time.sleep(2)
        myinfo.click_radio_save_btn()
        time.sleep(6)
        homepage.click_dropdown()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(1)

    def test_11_click_maritalstatus_dropdown(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        login = LoginPage(driver)
        login.enter_username('Admin')
        time.sleep(2)
        login.enter_password('admin123')
        time.sleep(2)
        login.press_login_btn()

        homepage = HomePage(driver)
        homepage.click_myinfo()
        time.sleep(2)

        myinfo = MyInfo(driver)
        myinfo.click_marital_dropdown()
        time.sleep(8)
        myinfo.click_smoker_radio_btn()
        time.sleep(6)
        myinfo.click_radio_save_btn()
        time.sleep(10)
        homepage.click_dropdown()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(1)


#         self.driver.find_element(By.NAME,'username').send_keys('Admin')
#         time.sleep(4)
#         self.driver.find_element(By.NAME,'password').send_keys('admin123')
#         time.sleep(4)
#         self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# # btn.click()
#         time.sleep(4)
#         self.driver.find_element(By.CLASS_NAME,'oxd-userdropdown-img').click()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
#         time.sleep(3)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


if __name__ == '__main__':
    # unittest.main(testRunner= HtmlTestRunner(output="C:\Users\usqgl\OneDrive\Desktop\Automationpycharm\Automationpycharm\POMProject\Files\Reports"))
    unittest.main()
