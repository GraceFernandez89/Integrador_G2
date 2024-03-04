# Problema: Filtrar números pares de una lista
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
# print("Lista original:", lista_numeros)
# print("Números pares:", numeros_pares)


# Problema: Filtrar cadenas que contienen la letra 'a'
# lista_cadenas = ["manzana", "banana", "cereza", "uva", "pera"]
# cadenas_con_a = list(filter(lambda x: 'a' in x, lista_cadenas))
# print("Lista original de cadenas:", lista_cadenas)
# print("Cadenas que contienen 'a':", cadenas_con_a)


# Problema: Filtrar números mayores que un valor en una lista
# lista_numeros = [15, 8, 25, 12, 10, 5, 30]
# valor_umbral = 15
# numeros_mayores_que_umbral = list(filter(lambda x: x > valor_umbral, lista_numeros))
# print("Lista original:", lista_numeros)
# print(f"Números mayores que {valor_umbral}:", numeros_mayores_que_umbral)

# Problema: Filtrar números primos de una lista
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lista_numeros = [2, 3, 5, 7, 10, 11, 13, 15, 17, 19, 20]
numeros_primos = list(filter(es_primo, lista_numeros))
print("Lista original de números:", lista_numeros)
print("Números primos:", numeros_primos)
