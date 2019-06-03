# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def test_untitled_test_case(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/")
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys("admin")
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys("secret")
        wb.find_element_by_xpath("//input[@value='Login']").click()
        wb.find_element_by_link_text("groups").click()
        wb.find_element_by_xpath("(//input[@name='new'])[2]").click()
        wb.find_element_by_name("group_name").click()
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys("name")
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys("11111")
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys("11111")
        wb.find_element_by_name("submit").click()
        wb.find_element_by_link_text("group page").click()
        wb.find_element_by_link_text("home").click()
        wb.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wb.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wb.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
