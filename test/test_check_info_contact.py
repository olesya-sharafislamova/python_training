import pytest


def test_check_info(app):
    with pytest.allure.step('Given a contact_from_home_page list'):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with pytest.allure.step('Given a contact_from_edit_page list'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then compare this lists'):
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page (contact):
    return "\n".join(filter(lambda x: x != "",
               filter(lambda x: x is not None, [contact.email, contact.email2,
                                                contact.email3])))