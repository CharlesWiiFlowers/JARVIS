"""
Communication with LLMs.

Every interaction with an LLM must to be here.
"""
from core.tool_manager import ToolManager
from core.events import events
import ollama

class LLM():
    def __init__(self, bus) -> None:
        self.bus = bus

        self.tool_manager = ToolManager(bus=self.bus)

        self.bus.on(
            events.LLM_USER_REQUEST_MESSAGE,
            self.get_response
        )

    def get_response(self):
        mensajes = [{'role': 'user', 'content': 'Jarvis, ejecuta un escaneo del sistema y dime qué fecha y hora es.'}]

        response = ollama.chat(
            model='Jarvis',  # <-- Aquí pones el nombre exacto que creaste
            messages=mensajes,
            tools=self.tool_manager.schemas()
        )

        self.bus.emit(
            events.LLM_RESPONSE,
            response
        )

        return response