import subprocess

herramienta_powershell = {
    'type': 'function',
    'function': {
        'name': 'ejecutar_powershell',
        'description': 'EJECUTA ESTA HERRAMIENTA OBLIGATORIAMENTE para obtener la fecha, hora o datos del sistema. NO asumas la respuesta ni des explicaciones teóricas.',
        'parameters': {
            'type': 'object',
            'properties': {
                'comando': {
                    'type': 'string',
                    'description': 'El comando exacto, ej: Get-Date'
                }
            },
            'required': ['comando']
        }
    }
}

def ejecutar_powershell(comando):
    # Ejecutamos el comando de forma invisible y capturamos el texto
    resultado = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True)
    return resultado.stdout.strip()

REGISTER = {
        "schema": herramienta_powershell,
        "handler": ejecutar_powershell,
        "enabled": True,
        "version": "0.1v-alpha",
        "author": "Flowers"
    }