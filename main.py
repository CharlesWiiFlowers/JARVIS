import ollama

print("🚀 [SISTEMA] Iniciando la conversación con Llama 3.1...")
msg = input("\nHABLA JAJA\n\n")

# 2. La función de Python que hará el trabajo sucio en tu PC

# Elimina el mensaje de 'system' que habíamos puesto en Python, porque Jarvis ya lo lleva en su ADN.
mensajes = [{'role': 'user', 'content': 'Jarvis, ejecuta un escaneo del sistema y dime qué fecha y hora es.'}]

respuesta = ollama.chat(
    model='Jarvis',  # <-- Aquí pones el nombre exacto que creaste
    messages=mensajes,
    tools=[herramienta_powershell]
)

# 5. Verificamos si Llama 3.1 decidió usar la herramienta o si respondió normal
if respuesta.get('message', {}).get('tool_calls'):
    
    # Extraemos qué herramienta pidió y qué comando nos mandó a ejecutar
    tool_call = respuesta['message']['tool_calls'][0]
    nombre_funcion = tool_call['function']['name']
    argumentos = tool_call['function']['arguments']
    
    print(f"🤖 [LLAMA] Solicitó la herramienta: {nombre_funcion} con argumentos: {argumentos}")

    if nombre_funcion == 'ejecutar_powershell':
        comando_solicitado = argumentos['comando']
        
        # --- LA ACCIÓN: Python ejecuta el PowerShell ---
        resultado_terminal = ejecutar_powershell(comando_solicitado)
        
        # 6. Agregamos lo sucedido al historial del chat para que Llama no pierda el hilo
        mensajes.append(respuesta['message']) # Guardamos que Llama pidió la herramienta
        mensajes.append({
            'role': 'tool',
            'content': resultado_terminal,
            'name': nombre_funcion
        }) # Guardamos la respuesta que nos dio la terminal de Windows
        
        print("🤖 [LLAMA] Analizando los datos del sistema...")
        
        # 7. Segundo envío: Llama lee el resultado de la herramienta y te responde humanamente
        respuesta_final = ollama.chat(
            model='llama3.1',
            messages=mensajes
        )
        
        print(f"\n✅ [IA]: {respuesta_final['message']['content']}")
else:
    # Si Llama 3.1 consideró que no necesitaba la herramienta, responde directo
    print(f"\n✅ [IA]: {respuesta['message']['content']}")