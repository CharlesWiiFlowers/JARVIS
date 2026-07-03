"""
Automatically loads every tool located in /tools.

Registers each tool and executes it whenever
the LLM requests it.
"""

import importlib
import pkgutil

from tools import __path__ as tools_path


class ToolManager:

    def __init__(self, bus):
        self.bus = bus

        self.tools = {}
        self.load_tools()

    def load_tools(self):

        for _, module_name, _ in pkgutil.iter_modules(tools_path):

            module = importlib.import_module(
                f"tools.{module_name}"
            )

            tool = module.REGISTER

            name = tool["schema"]["function"]["name"]

            self.tools[name] = tool

    def schemas(self):

        return [
            tool["schema"]
            for tool in self.tools.values()
        ]

    def execute(self, name, **kwargs):

        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")

        return self.tools[name]["handler"](**kwargs)