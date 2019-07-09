# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="oles", middlename="os", lastname="shar", nickname="osha", company="comp",
                      address="1111", homephone="495-1111111", mobilephone="9001111111", mail="qwe@ya.ru",
                      mail2="qwe@ya.ru", mail3="qwe@ya.ru", address2="qqqqq", notes="ajhspa")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







