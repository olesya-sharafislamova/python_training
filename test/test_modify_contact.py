
from model.contact import Contact

def test_mogify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "mikel")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert old_contacts == new_contacts
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
