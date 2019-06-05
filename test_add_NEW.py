# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group_contact import Group

class TestAddNEW(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_NEW(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, login="admin", password="secret")
        self.create_contact(wd, Group(firstname="olesya", lastname="shar", nickname="o.shar", address="111111", homephone="495-1111111", mobilephone="9001111111", mail="qwe@ya.ru", address2="qqqqq"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd, Group):
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Group.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Group.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Group.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Group.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Group.mobilephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Group.mail)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Group.address2)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
