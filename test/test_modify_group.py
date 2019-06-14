

def test_mogify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mogify_first_group(editname = "newname")
    app.session.logout()