
from model.group import Group

def test_mogify_group_name(app):
    app.group.mogify_first_group(Group(name = "new group"))


def test_mogify_group_header(app):
    app.group.mogify_first_group(Group(header = "new header"))
