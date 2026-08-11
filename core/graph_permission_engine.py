# -*- coding: utf-8 -*-


class GraphPermissionEngine:

    def __init__(self):

        self.permissions = {}

    def grant(self, user, permission):

        if user not in self.permissions:
            self.permissions[user] = set()

        self.permissions[user].add(permission)

        return True

    def revoke(self, user, permission):

        if user not in self.permissions:
            return False

        if permission not in self.permissions[user]:
            return False

        self.permissions[user].remove(permission)

        return True

    def has_permission(self, user, permission):

        return user in self.permissions and permission in self.permissions[user]

    def get_permissions(self, user):

        return list(self.permissions.get(user, set()))

    def info(self):

        return {
            "engine": "Graph Permission Engine",
            "version": "1.0",
            "users": len(self.permissions),
        }
