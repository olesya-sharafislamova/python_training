

class ContactHelper:

    def __init__ (self, app):
        self.app = app


    def create(self, contact):
        wb = self.app.wd
        # init new contact
        wb.find_element_by_link_text("add new").click()
        # fill contact form
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(contact.firstname)
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(contact.lastname)
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(contact.nickname)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(contact.address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(contact.homephone)
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(contact.mail)
        wb.find_element_by_name("address2").click()
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(contact.address2)
        # submit
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact (self):
        wb = self.app.wd
        # select first group
        wb.find_element_by_name("selected[]").click()
        # submit deletion
        wb.find_element_by_xpath(" //div[2]//input[1]").click()
        wb.switch_to_alert().accept()

    def mogify_first_contact (self, editcompany):
        wb = self.app.wd
        # check first contact
        wb.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]").click()
        # edit company
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(editcompany)
        wb.find_element_by_name("update").click()

    def count(self):
        wb = self.app.wd
        self.open_contact_page()
        return len (wb.find_elements_by_name("selected[]"))

    def open_contact_page(self):
        wb = self.app.wd
        if not ( len (wb.find_elements_by_link_text("Last name")) > 0):
            wb.find_element_by_link_text("home").click()