import re



def test_information_on_home_page_with_db(app, db):
    ui_list = app.contact.get_contact_list()
    for contact in ui_list:
        assert contact.firstname == (db.get_contact_by_id(contact.id).firstname).strip()
        assert contact.lastname == (db.get_contact_by_id(contact.id).lastname).strip()
        assert contact.address == (db.get_contact_by_id(contact.id).address).strip()
        assert contact.all_emails_from_home_page == all_emails_in_db(db.get_contact_by_id(contact.id))
        assert contact.all_phones_from_home_page == all_phones_in_db(db.get_contact_by_id(contact.id))



def clear(s):
    return re.sub("[() -]", "", s)

def all_emails_in_db(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

def all_phones_in_db(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.phone2]))))
