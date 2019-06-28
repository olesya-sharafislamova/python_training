# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="olesya", lastname="shar", nickname="o.shar", address="111111", homephone="495-1111111", mobilephone="9001111111", mail="qwe@ya.ru", address2="qqqqq"))
    app.contact.delete_first_contact()

