# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="oles", middlename="os", lastname="shar", nickname="osha", company="comp",
                      address="1111", homephone="4951111111", mobilephone="9001111111", workphone=495888888,
                      fax=495444444, mail="qwe@ya.ru", mail2="qwe@ya.ru", mail3="qwe@ya.ru",
                      address2="qqqqq", phone2="495-8522222", notes="ajhspa")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







