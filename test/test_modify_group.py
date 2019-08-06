
from model.group import Group
import random
import pytest


def test_mogify_group_name(app, db, check_ui):
    with pytest.allure.step('When add test data'):
        if app.group.count() == 0:
            app.group.create(Group(name = "test"))
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
        group_index = random.choice(range(len(old_groups)))
        id = old_groups[group_index].id
        group_to_modify = Group(name='New_name', id=id)
    with pytest.allure.step('When I edit a group'):
        app.group.modify_group_by_id(id, group_to_modify)
    with pytest.allure.step('Then compare the lists'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[group_index] = group_to_modify
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

