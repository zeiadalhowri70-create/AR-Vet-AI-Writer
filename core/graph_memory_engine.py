# -*- coding: utf-8 -*-


class GraphMemoryEngine:

    def __init__(self):

        self.memory = []

    def remember(self, item):

        self.memory.append(item)

        return True

    def recall(self, index=None):

        if index is None:
            return self.memory

        if index < len(self.memory):
            return self.memory[index]

        return None

    def forget(self, item):

        if item in self.memory:
            self.memory.remove(item)
            return True

        return False

    def clear(self):

        self.memory.clear()

        return True

    def info(self):

        return {
            "engine": "Graph Memory Engine",
            "version": "1.0",
            "items": len(self.memory),
        }
