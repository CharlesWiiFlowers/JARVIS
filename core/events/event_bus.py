"""
Event system.

Allows different modules to communicate
without depending on one another.
"""

from datetime import datetime

from core.events.events import Events
from core.events import event_types

class EventBus:

    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):
        """Subscribe to an event to call a function when somewhere emit the event.

        Args:
            event_name (str): Define a name to hear it.
            callback (function): The function to use the data when the event is on
        """

        if event_name not in self.listeners:
            self.listeners[event_name] = []

            # Notify: New event created
            self.emit(event_types.NEW_EVENT)

        self.listeners[event_name].append(callback)

    def on_all(self, callback):
        """Subscribe to every event

        Args:
            callback (function): The function to call whenever the events are on
        """

        for key in self.listeners:
            self.listeners[key].append(callback)


    def emit(self, event_name, data=None, source:object=None):

        if event_name not in self.listeners:
            return


        event = Events(
            event_type=event_name,
            data=data,
            timestamp=datetime.now(),
            source=source.__class__.__name__
        )

        for callback in self.listeners[event_name]:
            callback(event)