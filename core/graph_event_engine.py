# -*- coding: utf-8 -*-


class GraphEventEngine:

    def __init__(self):

        self.events = []

    def emit(self, event_type, data=None):

        event = {"type": event_type, "data": data or {}}

        self.events.append(event)

        return event

    def get_events(self):

        return self.events

    def last_event(self):

        if not self.events:
            return None

        return self.events[-1]

    def clear(self):

        self.events.clear()

        return True

    def info(self):

        return {
            "engine": "Graph Event Engine",
            "version": "1.0",
            "events": len(self.events),
        }
