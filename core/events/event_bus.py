"""
Event system.

Allows different modules to communicate
without depending on one another.
"""

class EventBus:

    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

    def emit(self, event_name, data=None):

        if event_name not in self.listeners:
            return

        for callback in self.listeners[event_name]:
            if data is not None:
                callback(data)
            else:
                callback()