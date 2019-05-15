import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import HtmlTestRunner



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C://Users/Aram/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Register(self):
        driver = self.driver
        driver.get("http://www.gcrit.com/build3/create_account.php")

        reg = Register(driver)
        reg.enter_email("aramro@hotmail.com")
        reg.enter_details1("Ara", "Lad", "05/07/1974 ", "aramro@hotmail.com", "Canadian Colledge",
                           "4630 dufferin", "m3h 5s4","Vaughan","on")

        reg.enter_details2("Canada", "4168907654")
        reg.enter_password("Colledge123", "Colledge123")
        reg.submit()





        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

            if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users/Aram/Downloads/chromedriver_win32/chromedriver.exe")

