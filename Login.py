#!/usr/bin/python3

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        path = "../drivers/chromedriver"
        self.driver = webdriver.Chrome(executable_path=path)
        
    def testLogIn(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        driver.find_element_by_class_name("login").click()
        driver.find_element_by_id("email").send_keys("aaa@jjj.com")
        driver.find_element_by_id("passwd").send_keys("12345")
        driver.find_element_by_id("SubmitLogin").click()
        checkLogin = driver.find_element_by_class_name("account").text
        #Added this pause so it is possible to follow the test result
        time.sleep(2)
        assert "Jessica Tavares" in checkLogin

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()