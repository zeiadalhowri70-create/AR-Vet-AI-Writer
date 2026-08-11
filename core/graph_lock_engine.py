# -*- coding: utf-8 -*-


class GraphLockEngine:

    def __init__(self):

        self.locks = set()

    def lock(self, resource):

        if resource in self.locks:
            return False

        self.locks.add(resource)

        return True

    def unlock(self, resource):

        if resource not in self.locks:
            return False

        self.locks.remove(resource)

        return True

    def is_locked(self, resource):

        return resource in self.locks

    def clear(self):

        self.locks.clear()

        return True

    def info(self):

        return {
            "engine": "Graph Lock Engine",
            "version": "1.0",
            "locks": len(self.locks),
        }
