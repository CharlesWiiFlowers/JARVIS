# J.A.R.V.I.S.

A modular, local-first AI assistant designed around plugins, events, and extensibility.

> [!IMPORTANT]
> J.A.R.V.I.S. is designed as a long-running local service rather than a traditional chatbot application.
> [!NOTE]
> This project is under active development. Internal APIs and modules may change as the architecture evolves.
> [!WARNING]
> Some tools may execute commands on the local machine. A security layer for privileged operations is planned but is not yet implemented.

---

## Overview

J.A.R.V.I.S. is a personal project that aims to build a persistent AI assistant inspired by the interaction model seen in the Iron Man films.

The main goal is not to replicate the movie version, but to build a practical assistant that can grow over time while remaining modular, easy to extend, and simple to maintain.

The assistant runs locally using Ollama and is designed to integrate with new tools, services, and external devices without requiring major changes to the existing codebase.

---

## Project Philosophy

The architecture is built around four core ideas:

* **Local-first** — Everything should work locally whenever possible.
* **Plugin-first** — New capabilities should be added without modifying existing code.
* **Event-driven** — Modules communicate through events instead of direct dependencies.
* **Plug and Play** — Expanding the assistant should require as little configuration as possible.

These principles guide every architectural decision made in the project.

---

## Current Capabilities

* [x] Local LLM execution using Ollama
* [x] Function calling
* [x] Automatic tool discovery
* [x] Modular service-based architecture
* [x] Event-driven communication
* [x] Prompt management
* [x] Configuration system
* [x] RSS news reader
* [x] Date and time retrieval

---

## Future Capabilities

* [ ] Speech interface (speech recognition and text-to-speech)
* [ ] Long-term memory
* [ ] IoT integration
* [ ] Local network communication
* [ ] Plugin SDK
* [ ] Desktop companion integration
* [ ] Multiple predefined assistant personalities
* [ ] Additional built-in tools

---

## Architecture

The assistant is divided into independent services.

```text
                User
                  │
                  ▼
             Assistant
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
     LLM                Tool Manager
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              Built-in Tools        Future Plugins
```

Each module has a single responsibility and should be replaceable without affecting the rest of the system.

---

## Project Structure

```text
core/
    Main application logic.

core/events/
    Event bus and event definitions.

tools/
    Built-in tools automatically loaded by the Tool Manager.

memory/
    Long-term memory and vector storage.

network/
    Network communication and future remote access.

speech/
    Speech recognition and speech synthesis.

ui/
    User interface components.

plugins/
    Future external extensions.

utils/
    Shared utilities used across the project.

data/
    Runtime configuration and generated data.

config/
    Ollama configuration and model-related files.
```

---

## Tool System

Every tool is completely self-contained.

Adding a new tool should not require modifying the rest of the project.

The only contract between a tool and J.A.R.V.I.S. is the exported `REGISTER` dictionary.

Example:

```python
REGISTER = {
    "schema": ...,
    "handler": execute,
    "enabled": True,
    "version": "1.0",
    "author": "Flowers"
}
```

This allows the Tool Manager to automatically discover, register, and execute new capabilities.

### Tool Principles

* A tool must be completely self-contained.
* A tool must not modify Jarvis internals.
* Adding a tool must not require changes to existing code.
* The only required interface is `REGISTER`.

---

## Current Built-in Tools

Current bundled tools include:

* RSS Reader
* Date and Time

Additional tools will be added as the project grows.

---

## Event System

The project follows an event-driven architecture.

Instead of calling each other directly, modules publish and listen for events.

For example:

```text
Speech
    │
    ▼
user_spoke
    │
    ▼
Assistant
    │
    ▼
tool_started
    │
    ▼
UI / Logger / Other Services
```

This reduces coupling between components and makes the system easier to expand.

---

## Runtime

| Component     | Technology          |
| ------------- | ------------------- |
| Language      | Python              |
| LLM Runtime   | Ollama              |
| Communication | Function Calling    |
| Architecture  | Event Driven        |
| Tool System   | Automatic Discovery |

---

## Hardware Requirements

> [!NOTE]
> The assistant's performance depends primarily on the selected language model and the available hardware. GPU VRAM is one of the main factors affecting response speed and model size.

---

## Contributing

Contributions, suggestions, and discussions are welcome ^^.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your work.
5. Open a Pull Request.

Please try to keep new features consistent with the project's architectural principles.

---

## License

This project is licensed under the GNU General Public License v3.0.

## Support

If you like this project, consider giving it a star on GitHub.

Every star is greatly appreciated ^^
