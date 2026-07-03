"""
General configuration for the project.
"""

from pathlib import Path
import json


class Config:
    DEFAULT_CONFIG = {
        "assistant_name": "Jarvis",
        "model": "llama3.1",
        "temperature": 0.7,
        "debug": True
    }

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent

        self.config_dir = self.project_root / "data"
        self.config_file = self.config_dir / "config.json"

        self.config_dir.mkdir(exist_ok=True)

        if not self.config_file.exists():
            self.data = self.DEFAULT_CONFIG.copy()
            self.save()
        else:
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.data = self.DEFAULT_CONFIG.copy()
                self.save()

    def save(self):
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value


config = Config()