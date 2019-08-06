# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import pytest

def test_delete_some_contact(app,db, check_ui):
    with pytest.allure.step('When add test data'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="olesya"))
    with pytest.allure.step('Given a Contact list'):
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then compare the lists'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
