
#Contador de palabras

# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Los caracteres que no contamos como palabras
quitar = ",;:.\n!\"'"
for caracter in quitar:
    text = text.replace(caracter,
                          "")  # Remplazarlo por "nada"; es decir, removerlo


# Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
text = text.lower()
# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = text.split(" ")

# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(frecuencia,palabra)