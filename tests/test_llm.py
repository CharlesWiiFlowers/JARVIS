"""
LLM Module Test
"""
import core.events.events as events

class TestLlm():
    def __init__(self, bus) -> None:
        self.bus = bus

        self.bus.on(
            events.LLM_RESPONSE,
            self.broadcaster
        )

        while True:
            self.bus.emit(
                events.LLM_USER_REQUEST_MESSAGE,
                input("Prompt:\n")
            )

    def broadcaster(self, data):
        print(data['message']['content'])