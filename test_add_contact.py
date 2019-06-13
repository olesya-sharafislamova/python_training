# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer (fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(firstname="olesya", lastname="shar", nickname="o.shar", address="111111", homephone="495-1111111", mobilephone="9001111111", mail="qwe@ya.ru", address2="qqqqq"))
    app.logout()

