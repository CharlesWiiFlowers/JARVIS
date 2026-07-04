"""
Makes the dynamic prompt
"""
from core.events.events import LLM_BUFFER_CONTEXT, LLM_BUFFER_UPDATED, LLM_RESPONSE

class Prompt():
    def __init__(self, bus) -> None:
        self.bus = bus
        self.context = ""

        self.bus.on(
            LLM_BUFFER_CONTEXT,
            self.add_context
        )

        self.bus.on(
            LLM_RESPONSE,
            self.append_conversation
        )
    
    def add_context(self, data):
        self.context = self.context + data['message']['content']

        self.bus.emit(
            LLM_BUFFER_UPDATED,
            self.context
        )

    def get_context(self):
        return self.context
    
    def append_conversation(self, response):
        self.add_context(response)