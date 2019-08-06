from model.contact import Contact
from model.group import Group
import random
import pytest



def test_add_contact_in_group(app,db, orm):
    with pytest.allure.step('When add test data'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="olesya"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="name3", header="header3", footer="footer3"))
    with pytest.allure.step('Given a group list'):
        contact_list = db.get_contact_list()
        group_list = db.get_group_list()
        contact_id = random.choice(contact_list).id
        group_id = random.choice(group_list).id
    with pytest.allure.step('When I add contact in group'):
        app.contact.add_contact_in_group(contact_id, group_id)
    with pytest.allure.step('Then compare the lists'):
        assert db.get_contact_by_id(contact_id) in orm.get_contacts_in_group(Group(id=group_id))