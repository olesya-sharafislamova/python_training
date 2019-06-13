
class GroupHelper:

    def __init__ (self, app):
        self.app = app


    def open_group_page(self):
        wb = self.app.wd
        wb.find_element_by_link_text("groups").click()

    def create(self, group):
        wb = self.app.wd
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

    def delete_first_group(self):
        wb = self.app.wd
        self.open_group_page()
        # select first group
        wb.find_element_by_name("selected[]").click()
        # submit deletion
        wb.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wb = self.app.wd
        wb.find_element_by_link_text("group page").click()
