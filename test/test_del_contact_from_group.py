from model.contact import Contact
from model.group import Group
import random
import pytest


def test_delete_contact_from_group(app, db, orm):
    with pytest.allure.step('When add test data'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="olesya"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="name3", header="header3", footer="footer3"))
        if len(db.get_groups_with_contacts())==0:
            contact_id = random.choice(db.get_contact_list()).id
            group_id = random.choice(db.get_group_list()).id
            app.contact.add_contact_in_group(contact_id, group_id)

        group_id = random.choice(db.get_groups_with_contacts()).id
        contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    with pytest.allure.step('Given delete contact from group'):
        app.contact.delete_contact_from_group(group_id)
    with pytest.allure.step('Then check'):
        assert db.get_contact_by_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))