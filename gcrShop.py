import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
#import HTMLTestRunner
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C://Users/Aram/Downloads/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://www.gcrit.com/build3/create_account.php")
driver.find_element_by_xpath("//input[@name='email_address']").send_keys("aramro@hotmail.com")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[2]").click()

driver.find_element_by_xpath("//input[@name='firstname']").send_keys("Ara")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Lad")
driver.find_element_by_xpath("//input[@id='dob']").send_keys("05/07/1974")
driver.find_element_by_xpath("//input[@name='company']").send_keys("Canadian Colledge")

driver.find_element_by_xpath("//input[@name='street_address']").send_keys("4630 dufferin")
driver.find_element_by_xpath("//input[@name='postcode']").send_keys("m3h 5s4")
driver.find_element_by_xpath("//input[@name='city']").send_keys("Vaughan")
driver.find_element_by_xpath("//input[@name='state']").send_keys("on")

element1= driver.find_element_by_xpath("//select[@name='country']")
drp = Select(element1)
drp.select_by_visible_text("Canada")

driver.find_element_by_xpath("//input[@name='telephone']").send_keys("4168907654")
driver.find_element_by_xpath("//input[@name='password']").send_keys("Colledge123")
driver.find_element_by_xpath("//input[@name='confirmation']").send_keys("Colledge123")
driver.find_element_by_xpath(" //span[contains(text(),'Continue')]").click()


