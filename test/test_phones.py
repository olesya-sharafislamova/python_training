import re
import pytest

def test_phones_on_home_page(app):
    with pytest.allure.step('Given contact_from_home_page and contact_from_edit_page'):
        contact_from_home_page = app.contact.get_contact_list()[0]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then compare phones on home page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)



def test_phones_on_contact_view_page(app):
    with pytest.allure.step('Given contact_from_home_page and contact_from_edit_page'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then compare phones on view page'):
        assert contact_from_view_page.homephone == contact_from_edit_page.homephone
        assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
        assert contact_from_view_page.workphone == contact_from_edit_page.workphone
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page (contact):
    return "\n".join(filter(lambda x: x != "",
               map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                        contact.workphone, contact.phone2]))))