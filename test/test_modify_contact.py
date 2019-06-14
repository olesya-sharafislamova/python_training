

def test_mogify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.mogify_first_contact(editcompany = "company")
    app.session.logout()