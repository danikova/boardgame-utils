from apps.common.group import Group


class GroupManager(object):
    def __init__(self):
        self.groups = {}

    def get_group_by_id(self, group_id):
        group_id = str(group_id)
        if group_id in self.groups:
            return self.groups[group_id]
        return None

    def get_or_create_group_by_id(self, group_id):
        group_id = str(group_id)
        if group_id in self.groups:
            return self.groups[group_id]
        else:
            new_group = Group(group_id)
            self.groups[group_id] = new_group
            print(f'Manager: new group created {group_id}')
            return new_group

    def remove_group_when_it_has_no_connections(self, group_id):
        group_id = str(group_id)
        if group_id in self.groups:
            group = self.groups[group_id]
            if not group.sockets:
                del self.groups[group_id]
                print(f'Manager: empty group deleted {group_id}')
