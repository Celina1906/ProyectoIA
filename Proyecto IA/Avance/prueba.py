import openai
from googletrans import Translator

# Configurar clave de API de OpenAI
openai.api_key = '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'

# Interactuar con la API de ChatGPT
def obtener_respuesta(prompt1):
    response = openai.Completion.create(
        engine="text-davinci-003",  #motor
        prompt=prompt1,
        max_tokens=2048  
    )
    return response.choices[0].text

# Usar la función para obtener respuestas
print()
historia = input("Dame la sinopsis de tu historia: ")
print()
prompt1 = "Crea una historia de " + historia
respuestaEs = obtener_respuesta(prompt1)
print("Historia en español")
print(respuestaEs+"\n")

translator = Translator()

respuestaEn = translator.translate(respuestaEs, src="es", dest="en")
print("Historia en inglés\n")
print(respuestaEn.text+"\n")

response = openai.Image.create(
  prompt=historia,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)