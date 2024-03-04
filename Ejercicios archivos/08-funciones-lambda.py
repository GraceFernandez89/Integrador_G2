

#Filtrar números mayores que un valor en una lista:
# lista = [1, 10, 5, 8, 3, 12]

# filtrar_mayores_que_cinco = lambda lista: list(filter(lambda x: x > 5, lista))

# resultado_filtrado = filtrar_mayores_que_cinco(lista)
# print("Números mayores que cinco:", resultado_filtrado)


#Concatenar dos cadenas:

concatenar = lambda cadena1, cadena2: cadena1 + " " + cadena2

saludo = concatenar("Hola", "Mundo")
print("Saludo:", saludo)

#Verificar si un número es par:
es_par = lambda x: x % 2 == 0

numero = 6
print(f"¿{numero} es par?: {es_par(numero)}")





