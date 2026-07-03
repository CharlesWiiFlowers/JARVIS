from pathlib import Path

PROJECT_NAME = "Jarvis"

files = {
    "main.py":
"""\"\"\"
Punto de entrada del proyecto.

Inicializa todos los servicios principales y mantiene vivo el asistente.
Aquí NO debería existir lógica complicada; solamente arrancar el sistema.
\"\"\"
""",

    "README.md":
"""# Jarvis

Proyecto personal de Carlitos.

Arquitectura basada en servicios, plugins y eventos.
""",

    "requirements.txt":
"""# Dependencias del proyecto
""",

    # ==========================
    # CORE
    # ==========================

    "core/__init__.py": "",

    "core/assistant.py":
'''"""
Coordinador principal del sistema.

Recibe eventos, conversa con el LLM y coordina
los demás módulos.
"""
''',

    "core/llm.py":
'''"""
Comunicación con el modelo de lenguaje.

Toda interacción con Ollama, OpenAI o cualquier
otro modelo debe pasar por aquí.
"""
''',

    "core/tool_manager.py":
'''"""
Carga automáticamente todas las herramientas
ubicadas en /tools.

Debe registrar cada herramienta y ejecutarla
cuando el LLM la solicite.
"""
''',

    "core/event_bus.py":
'''"""
Sistema de eventos.

Permite que los distintos módulos se comuniquen
sin depender unos de otros.
"""
''',

    "core/prompt.py":
'''"""
Prompt del sistema.

Aquí vive la personalidad y reglas de Jarvis.
"""
''',

    "core/config.py":
'''"""
Configuraciones generales del proyecto.
"""
''',

    # ==========================
    # TOOLS
    # ==========================

    "tools/__init__.py": "",

    "tools/get_hour.py":
'''"""
Obtiene la fecha y hora del sistema.
"""
''',

    "tools/powershell.py":
'''"""
Ejecuta comandos de PowerShell de forma segura.

Todas las herramientas que necesiten PowerShell
deberían reutilizar este módulo.
"""
''',

    "tools/calculator.py":
'''"""
Realiza operaciones matemáticas.
"""
''',

    # ==========================
    # UI
    # ==========================

    "ui/__init__.py": "",

    "ui/window.py":
'''"""
Ventana principal del asistente.
"""
''',

    "ui/animations.py":
'''"""
Controla las animaciones del personaje.

Idle
Listening
Thinking
Speaking
Happy
Sleeping
"""
''',

    "ui/character.py":
'''"""
Representación visual del personaje.
"""
''',

    "ui/assets/.gitkeep": "",

    # ==========================
    # SPEECH
    # ==========================

    "speech/__init__.py": "",

    "speech/speech_to_text.py":
'''"""
Convierte voz en texto.
"""
''',

    "speech/text_to_speech.py":
'''"""
Convierte texto en voz.
"""
''',

    "speech/wake_word.py":
'''"""
Detecta la palabra de activación.
"""
''',

    # ==========================
    # MEMORY
    # ==========================

    "memory/__init__.py": "",

    "memory/embeddings.py":
'''"""
Generación de embeddings.
"""
''',

    "memory/vector_store.py":
'''"""
Base de conocimiento vectorial.
"""
''',

    "memory/history.py":
'''"""
Historial de conversaciones.
"""
''',

    # ==========================
    # NETWORK
    # ==========================

    "network/__init__.py": "",

    "network/api.py":
'''"""
API HTTP para controlar Jarvis.
"""
''',

    "network/websocket.py":
'''"""
Servidor WebSocket para comunicación en tiempo real.
"""
''',

    "network/discovery.py":
'''"""
Descubre automáticamente otros dispositivos
en la red local.
"""
''',

    # ==========================
    # UTILS
    # ==========================

    "utils/__init__.py": "",

    "utils/logger.py":
'''"""
Sistema de logs del proyecto.
"""
''',

    "utils/colors.py":
'''"""
Colores y estilos para la consola.
"""
''',

    "utils/helpers.py":
'''"""
Funciones auxiliares reutilizables.
"""
''',

    # ==========================
    # TESTS
    # ==========================

    "tests/__init__.py": "",

    "tests/test_tools.py":
'''"""
Pruebas para las herramientas.
"""
''',

    "tests/test_llm.py":
'''"""
Pruebas del módulo LLM.
"""
''',
}

root = Path(PROJECT_NAME)

for file, content in files.items():
    path = root / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

print(f"Proyecto '{PROJECT_NAME}' creado correctamente.")