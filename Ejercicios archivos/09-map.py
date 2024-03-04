# Problema: Duplicar cada elemento en una lista
# lista_original = [1, 2, 3, 4, 5]
# lista_duplicada = list(map(lambda x: x * 2, lista_original))
# print("Lista original:", lista_original)
# print("Lista duplicada:", lista_duplicada)


# Problema: Obtener la longitud de cada cadena en una lista de cadenas
# lista_cadenas = ["Hola", "Mundo", "Python"]
# longitudes = list(map(lambda x: len(x), lista_cadenas))
# print("Lista de cadenas:", lista_cadenas)
# print("Longitudes correspondientes:", longitudes)


# Problema: Elevar al cuadrado cada elemento en una lista
# lista_numeros = [2, 3, 5, 7, 11]
# cuadrados = list(map(lambda x: x ** 2, lista_numeros))
# print("Lista original:", lista_numeros)
# print("Cuadrados de cada elemento:", cuadrados)


# Problema: Concatenar un prefijo a cada elemento en una lista de palabras
palabras = ["manzana", "banana", "cereza"]
prefijo = "fruta_"
palabras_con_prefijo = list(map(lambda x: prefijo + x, palabras))
print("Lista original de palabras:", palabras)
print("Palabras con prefijo:", palabras_con_prefijo)