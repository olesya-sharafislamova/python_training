
import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True


    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_by_id(self, id_cont):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, home, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated = '0000-00-00 00:00:00' and id='%s'" % id_cont)
            for row in cursor:
                (id, firstname, lastname, address, mobile, home, work, phone2, email, email2, email3) = row
                contact_sel = (Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                       homephone=home, mobilephone=mobile, workphone=work, phone2=phone2, email=email,
                                       email2=email2, email3=email3))
        finally:
            cursor.close()
        return contact_sel

    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(Group(id=str(id)))

        finally:
            cursor.close()
        return list
