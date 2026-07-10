# EventBus

The EventBus is the communication backbone of Jarvis.

Its purpose is to allow independent modules to communicate without creating direct dependencies between them. Instead of modules calling each other directly, they communicate by emitting and listening for events.

This architecture makes the system easier to extend, maintain, debug, and scale.

---

# Why use an EventBus?

Without an EventBus:

```
LLM
 ├── UI
 ├── Voice
 ├── Logger
 └── Memory
```

The LLM needs to know every module that depends on its output.

This creates strong coupling between components.

With an EventBus:

```
              EventBus
          /      |      \
         /       |       \
       UI      Voice    Logger
         \      |       /
             Memory

                ▲
                |
               LLM
```

The LLM only emits an event.

Every interested module decides independently if it wants to react.

---

# Core concepts

## Events

An event represents something that happened inside the system.

Examples:

* `USER_MESSAGE`
* `LLM_RESPONSE`
* `TOOL_STARTED`
* `TOOL_FINISHED`
* `VOICE_STARTED`

Events describe **what happened**, not **how it happened**.

---

## Event object

Every emitted event is wrapped inside an `Event` object.

The Event object contains useful metadata:

```python
Event(
    event_type="LLM_RESPONSE",
    data=response,
    timestamp=datetime.now(),
    source="LLM"
)
```

Available information:

| Field        | Description                          |
| ------------ | ------------------------------------ |
| `event_type` | The name of the event                |
| `data`       | Information transmitted by the event |
| `timestamp`  | When the event was emitted           |
| `source`     | The module that emitted the event    |

The EventBus creates this object automatically when an event is emitted.

Modules only need to provide the event name and optional data.

---

# Listeners

A listener is a callback function executed whenever a specific event is emitted.

Example:

```python
bus.on(
    Events.LLM_RESPONSE,
    ui.display_message
)
```

This registers `display_message()` to be executed whenever `LLM_RESPONSE` occurs.

A listener receives the complete `Event` object:

```python
def display_message(event: Event):

    print(event.data)
```

---

# Global listeners

Some modules need to observe everything that happens in the system.

Examples:

* Logger
* Debug tools
* Metrics
* Monitoring systems

For these cases, the EventBus provides global listeners.

Example:

```python
bus.on_all(
    logger.save
)
```

The callback will receive every emitted event.

---

# Emitting an event

When a module finishes an action, it announces it through the EventBus.

Example:

```python
bus.emit(
    Events.LLM_RESPONSE,
    response,
    source=llm
)
```

The EventBus automatically creates:

```python
Event(
    event_type=Events.LLM_RESPONSE,
    data=response,
    timestamp=current_time,
    source="LLM"
)
```

and sends it to all registered listeners.

---

# Internal events

The EventBus can also emit events about itself.

Examples:

* `EVENT_NEW` - A new event type was registered.
* `EVENT_EMIT` - An event was emitted.

These events allow debugging and system monitoring.

Internal events should be handled carefully to avoid recursive event loops.

---

# Design philosophy

The EventBus should remain as simple as possible.

Its responsibilities are limited to:

* Register listeners.
* Emit events.
* Create Event objects.
* Notify listeners.

It should **not** contain application logic.

Business logic belongs to the modules that emit or receive events.

---

# Current API

## Register a listener

```python
bus.on(
    event_name,
    callback
)
```

Registers a callback for a specific event.

---

## Register a global listener

```python
bus.on_all(
    callback
)
```

Registers a callback that receives every event.

---

## Emit an event

```python
bus.emit(
    event_name,
    data,
    source
)
```

Creates and sends an Event object to all listeners.

Example:

```python
bus.emit(
    Events.USER_MESSAGE,
    "Hello Jarvis",
    source=voice
)
```

---

# Advantages

* Low coupling between modules.
* Easy to add new features.
* Easier testing.
* Plugins can subscribe to existing events.
* Multiple modules can react to the same event.
* Modules remain independent.
* System behavior can be observed through global listeners.

---

# Example

```python
bus.on(
    Events.LLM_RESPONSE,
    speech.speak
)

bus.on(
    Events.LLM_RESPONSE,
    logger.save
)

bus.on(
    Events.LLM_RESPONSE,
    ui.display
)

bus.emit(
    Events.LLM_RESPONSE,
    response,
    source=llm
)
```

In this example, Speech, Logger, and UI all react to the same event without knowing each other exists.

---

# Future improvements

Possible additions:

* Listener removal (`off()`).
* Listener priorities.
* Asynchronous events.
* Sticky events.
* Event replay.
* Event debugging tools.
* Exception isolation for listeners.

These features should only be added when needed, keeping the EventBus lightweight, predictable, and easy to maintain.
