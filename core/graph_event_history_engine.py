# -*- coding: utf-8 -*-

from datetime import datetime


class GraphEventHistoryEngine:

    def __init__(self):

        self.history = []

    def add(self, event_type, details=None):

        event = {
            "type": event_type,
            "details": details or {},
            "time": datetime.now().isoformat(),
        }

        self.history.append(event)

        return event

    def all(self):

        return self.history

    def count(self):

        return len(self.history)

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def clear(self):

        self.history.clear()

        return True

    def info(self):

        return {
            "engine": "Graph Event History Engine",
            "version": "1.0",
            "events": len(self.history),
        }
