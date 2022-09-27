
#Contador de palabras

# pip install -U spacy
# python -m spacy 
import spacy

# Descargar y Cargar en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = input("Ingrese el texto: ")
doc = nlp(text)

# Los caracteres que no contamos como palabras
quitar = ",;:.\n!\"'"
for caracter in quitar:
    text = text.replace(caracter,
                          "")  # Remplazarlo por "nada"; es decir, removerlo


# Convertimos toda palabra a minúscula
text = text.lower()
# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = text.split(" ")

# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
Diccionario = {}
for palabra in palabras:
    if palabra in Diccionario:
        Diccionario[palabra] += 1
    else:
        Diccionario[palabra] = 1

for palabra in Diccionario:
    frecuencia = Diccionario[palabra]
    print(frecuencia,palabra)
