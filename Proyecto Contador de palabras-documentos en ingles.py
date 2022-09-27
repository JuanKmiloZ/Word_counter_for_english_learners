
#Contador de palabras

# Insertar documents
texto = input("Ingrese el texto: ")

# Quitar caracteres que no son palabras
excluir = ",;:.\n!\"'"
for caracter in excluir:
    texto = texto.replace(caracter,
                          "")  # Remplazarlo por "nada"; es decir, removerlo


# Convertimos toda palabra a minúscula
texto = texto.lower()

# Las palabras se separan con split
palabras = texto.split(" ")

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
