import subprocess

get_hour = {
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

def execute(comando):
    # Ejecutamos el comando de forma invisible y capturamos el texto
    resultado = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True)
    return {
        "success": True,
        "content": resultado.stdout.strip()
    }.__str__()

REGISTER = {
        "schema": get_hour,
        "handler": execute,
        "enabled": True,
        "version": "0.1v-alpha",
        "author": "Flowers"
    }