import os
from google import genai
from google.genai import types

# 1. Configuración: El cliente busca automáticamente la clave API
#    en la variable de entorno GEMINI_API_KEY.
try:
    # Intenta inicializar el cliente de Gemini
    client = genai.Client()
    print("✅ Conexión con la API de Gemini establecida.")
except Exception as e:
    # Muestra un mensaje de error si la clave no está configurada
    print("❌ ERROR: No se pudo conectar.")
    print("Por favor, configura la variable de entorno GEMINI_API_KEY en tu terminal.")
    exit()


# 2. Función principal para generar el código
def generar_snippet_python(peticion_usuario):
    """
    Envía la petición del usuario a la IA, usando el prompt de "Experto en Sintaxis",
    para obtener un fragmento de código Python limpio y listo para usar.
    """

    # 3. El PROMPT COMPLETO: Instrucciones detalladas para forzar la respuesta a ser solo código
    prompt = f"""
Eres un Experto en Sintaxis de Python 3.x. Tu misión es traducir peticiones de lenguaje natural a fragmentos de código Python idiomático, conciso y funcional. Nunca respondas con texto explicativo ni conversacional. Tu única respuesta debe ser el bloque de código. Si se necesita una importación, esta debe ser la primera línea. El código debe ser una solución completa y lista para usar.

Ejemplo:
Petición: Quiero poner una frase en mayúscula
Respuesta:
```python
frase = "hola mundo"
frase_mayus = frase.upper()
Petición: {peticion_usuario} Respuesta: """


# 4. Configuración del modelo: Temperatura baja (0.1) para priorizar la precisión y la lógica
config = types.GenerateContentConfig(
    temperature=0.1,
)

# 5. Llamada a la API (usando el modelo rápido y económico 'gemini-2.5-flash')
try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=config,
    )
    return response.text
except Exception as e:
    return f"Error en la llamada a la API: {e}"
--- LÓGICA
DE
INTERACCIÓN
POR
TERMINAL - --
if name == "main": print("\n=============================================")
print(" Asistente de Sintaxis Python (Gemini)")
print("=============================================")

# Solicita la pregunta al usuario
peticion_usuario = input("➡️ Escribe tu duda de código (ej. 'quiero filtrar una lista'): ")

if not peticion_usuario.strip():
    print("❌ Por favor, introduce una pregunta válida.")
else:
    print("\n⏳ Generando código...")

    # Llama a la función
    codigo_generado = generar_snippet_python(peticion_usuario)

    # Muestra el resultado
    print("\n--- Respuesta de Código Generado ---")
    print(codigo_generado)
    print("------------------------------------")