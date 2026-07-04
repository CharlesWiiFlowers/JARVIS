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

        self.context = ""

        self.bus.on(
            events.LLM_USER_REQUEST_MESSAGE,
            self.get_response
        )

        self.bus.on(
            events.LLM_BUFFER_UPDATED,
            self.get_context
        )

    def get_response(self, data):
        prompt = [
            {'role': 'system', 'content': f'{self.context}'},
            {'role': 'user', 'content': f'Jarvis, {data}'}]

        response = ollama.chat(
            model='Jarvis',  # <-- Aquí pones el nombre exacto que creaste
            messages=prompt,
            tools=self.tool_manager.schemas()
        )

        if response.get('message', {}).get('tool_calls'):
            tool_call = response['message']['tool_calls'][0]
            function_name = tool_call['function']['name']
            args = tool_call['function']['arguments']

            prompt.append(response['message'])
            prompt.append(
                {
                    "role": "tool",
                    "content": self.tool_manager.execute(
                        function_name,
                        **args
                    ),
                    "name": function_name
                }
            )

            response = ollama.chat(
                model='Jarvis',  # <-- Aquí pones el nombre exacto que creaste
                messages=prompt,
                tools=self.tool_manager.schemas()
            )


        self.bus.emit(
            events.LLM_RESPONSE,
            response
        )

        return response
    
    def get_context(self, data):
        self.context = data