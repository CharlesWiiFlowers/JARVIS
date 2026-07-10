"""
LLM Module Test
"""
from core.events import event_types
from core.events.event_bus import EventBus
from core.events.events import Event

class TestLlm():
    def __init__(self, bus: EventBus) -> None:
        self.bus = bus

        self.bus.on(
            event_types.LLM_RESPONSE,
            self.broadcaster
        )

        while True:
            self.bus.emit(
                event_types.LLM_USER_REQUEST_MESSAGE,
                input("Prompt:\n")
            )

    def broadcaster(self, event:Event):
        print(event.data['message']['content'])