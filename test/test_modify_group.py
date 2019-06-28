
from model.group import Group

def test_mogify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.mogify_first_group(Group(name = "new group"))


def test_mogify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.mogify_first_group(Group(header = "new header"))
