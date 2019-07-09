
from model.group import Group

def test_mogify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name = "new group")
    group.id = old_groups[0].id
    app.group.mogify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_mogify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    app.group.mogify_first_group(Group(header = "new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
