
from model.contact import Contact
import random
import pytest


def test_modify_first_contact(app, db, check_ui):
    with pytest.allure.step('When add test data'):
        if len(db.get_contact_list()) == 0:
            app.contact.create_new_contact(
                Contact(firstname="test", middlename="middlename"))

        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

    with pytest.allure.step('Given a Contact list'):
        old_contacts = db.get_contact_list()
        contact_index = random.choice(range(len(old_contacts)))
        id = old_contacts[contact_index].id
        contact_modify = Contact(firstname="New_firstname", id=id)
    with pytest.allure.step('When I edit a contact'):
        app.contact.modify_contact_by_id(id, contact_modify)
    with pytest.allure.step('Then compare the lists'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[contact_index] = contact_modify
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                     key=Contact.id_or_max)

