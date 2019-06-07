from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wb = self.wd
        wb.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wb = self.wd
        self.open_group_page()
        # init group creation
        wb.find_element_by_xpath("(//input[@name='new'])[2]").click()
        # fill group firm
        wb.find_element_by_name("group_name").click()
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys(group.name)
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys(group.header)
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wb = self.wd
        wb.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wb = self.wd
        self.open_home_page()
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wb = self.wd
        wb.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()