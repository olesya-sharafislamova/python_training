

class GroupHelper:

    def __init__ (self, app):
        self.app = app

    def open_group_page(self):
        wb = self.app.wd
        if not (wb.current_url.endswith("/group.php") and len (wb.find_elements_by_name("new")) > 0):
            wb.find_element_by_link_text("groups").click()

    def create(self, group):
        wb = self.app.wd
        self.open_group_page()
        # init group creation
        wb.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.fill_group_firm(group)
        # submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group (self):
        wb = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wb.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wb = self.app.wd
        wb.find_element_by_link_text("group page").click()

    def mogify_first_group (self, new_group_data):
        wb = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wb.find_element_by_name("edit").click()
        self.fill_group_firm(new_group_data)
        # submit modification
        wb.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wb = self.app.wd
        wb.find_element_by_name("selected[]").click()

    def fill_group_firm(self, group):
        wb = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wb = self.app.wd
        if text is not None:
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wb = self.app.wd
        self.open_group_page()
        return len (wb.find_elements_by_name("selected[]"))
