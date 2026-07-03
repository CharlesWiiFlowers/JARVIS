from core.tool_manager import ToolManager
from core.events.event_bus import EventBus
from core.llm import LLM
from core.config import Config

class Main():
    def __init__(self):
        self.bus = EventBus()

        self.tool_manager = ToolManager(bus=self.bus)
        self.llm = LLM(bus=self.bus)
        
        self.config = Config()

        if self.config.get("debug"):
            from tests.test_llm import TestLlm
            self.test = TestLlm(bus=self.bus)
        

if __name__ == "__main__":
    main = Main()