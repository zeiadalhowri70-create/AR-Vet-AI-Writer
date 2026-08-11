# -*- coding: utf-8 -*-


class ProviderQueueEngine:

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)
        return len(self.queue)

    def items(self):
        return self.queue

    def info(self):
        return {
            "engine": "Provider Queue Engine",
            "version": "1.0",
            "size": len(self.queue),
        }
