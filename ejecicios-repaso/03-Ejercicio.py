# texto = input("Ingrese un texto: ").lower()
# lista = []
# for i in range(3):
#     letra = input("Ingrese una letra: ")
#     lista.append(letra)
# frecuencia = {}
# for i in texto:
#     if i in lista:
#         if i in frecuencia:
#             frecuencia[i] += 1
#         else:
#             frecuencia[i] = 1
# print("La frecuencia de las letras ingresadas son: ")
# for i, n in frecuencia.items():
#     print(f"{i}: {n}")
    
    
    

    
# texto = input("Ingrese un texto: ").lower()
# letra1 = input("Ingrese una letra: ").lower()
# letra2 = input("Ingrese otra letra: ").lower()
# letra3 = input("Ingrese otra letra: ").lower()
# listaLetra = [letra1, letra2, letra3]
# canletra1 = texto.count(listaLetra[0])
# canletra2 = texto.count(listaLetra[1])
# canletra3 = texto.count(listaLetra[2])
# print(f"""{letra1} aparece {canletra1} veces
# {letra2} aparece {canletra2} veces
# {letra3} aparece {canletra3} veces""")    


# def contar(palabra, l):
#   p=palabra.lower()
#   return p.count(l.lower())
# if __name__ == "__main__":
#     t=input("ingrese un texto al programa ")
#     for i in range(0,3):
#         l=input("ingresa una letra ")
#         print(contar(t,l))



# text = input("ingrese un texto de su elección: ").lower()
# letters = input("ingrese tres letras: ").lower()
# while (len(letters) != 3 ):
#     letters = input("ingrese tres letras: ").lower()
# first = text.count(letters[0])
# second = text.count(letters[1])
# third = text.count(letters[2])
# print(f"en el texto existen {first} letras {letters[0]}, {second} letras {letters[1]} y {third} letras {letters[2]}")


# Texto = input ("Por favor ingrese un texto: ")
# Texto.lower()
# letras = list(input ("Por favor ingrese tres letras: "))
# print(letras)

# print(letras.count(letras))
# frecuencias = [Texto.count(letra) for letra in letras]


# for letra, frecuencia in zip(letras, frecuencias):
#     print(f"La letra '{letra}' aparece {frecuencia} veces en el texto.")


# def contar_letras(texto, letras):
#     contador = {}
#     for letra in letras:
#         contador[letra] = texto.count(letra)
#     return contador


# texto = input("Ingresa una cadena de texto o texto: ").lower()
# letra1 = input("Ingresa la primera letra: ").lower()
# letra2 = input("Ingresa la segunda letra: ").lower()
# letra3 = input("Ingresa la tercera letra: ").lower()

# letras = [letra1, letra2, letra3]

# resultado = contar_letras(texto, letras)

# print("Resultados:")
# for letra, cantidad in resultado.items():
#     print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")


# texto = input("ingresa un texto: ")
# letras = input("Ingresa tres letras : ")
# texto = texto.lower()
# letras = letras.lower()
# contador_letras = {}
# for letra in letras:
#     contador_letras[letra] = texto.count(letra)
# print("la Cantidad de veces que aparece cada letra:")
# for letra, cantidad in contador_letras.items():
#     print(f"{letra}: {cantidad}")

# Santiago Enrique Bastidas Estrada  to  Everyone 8:42 PM
# texto = input("Ingrese un texto ->").lower()
# letra1 = input("Ingrese letra 1 ->").lower()
# letra2 = input("Ingrese letra 2 ->").lower()
# letra3 = input("Ingrese letra 3 ->").lower()
# lista = [letra1,letra2,letra3]
# for letra in lista:
#     cantidad = texto.count(letra)
#     print(f"Cuantas veces aparece {letra} en {texto} es: {cantidad}")

# YefersonQ  to  Everyone 8:42 PM
# def get_texto():
#     return input("Por favor, ingrese el texto: ")
# def get_letras():
#     letras = []
#     for i in range(3):
#         letter = input(f"Por favor, ingrese la letra {i+1}: ")
#         letras.append(letter)
#     return letras
# def count_letras(texto, letras):
#     texto = texto.lower()
#     contador = []
#     for letter in letras:
#         count = texto.count(letter.lower())
#         contador.append(count)
#     return contador
# def print_contador(letras, contador):
#     for i in range(3):
#         print(f"La letra '{letras[i]}' aparece {contador[i]} veces en el textoo.")
# def main():
#     texto = get_texto()
#     letras = get_letras()
#     contador = count_letras(texto, letras)
#     print_contador(letras, contador)
# main()

# charf  to  Everyone 8:45 PM
# cadena = input("ingresa un texto").lower()
# l1 = input("Ingresa letra uno").lower()
# l2 = input("Ingresa letra dos").lower()
# l3 = input("Ingresa letra tres").lower()

# listaletras = [l1, l2, l3]
# contarletras= 0

# for i in cadena:
#     if i in listaletras:
#         contarletras += 1


# print(contarletras)

# Jhon Jairo Muñoz Gironza  to  Everyone 8:45 PM
# def contar_letras(texto, letras):
#     contador = {letra: 0 for letra in letras}
#     for letra in texto:
#         if letra in contador:
#             contador[letra] += 1
#     return contador

# texto = input("Ingresa un texto: ")
# letras = input("Ingresa las 3 letras separadas: ").split()

# if len(letras) != 3:
#     print("ingresa exactamente 3 letras.")
# else:
#     resultado = contar_letras(texto, letras)
#     for letra, cantidad in resultado.items():
#         print(f"La letra '{letra}' aparece {cantidad} veces.")

# AngieGuerrero 8:46 PM
# text = input("Enter your information: ").lower()
# aux = 0
# letters = []
# while (aux<3):
#     aux+=1
#     letter = input("Enter letter: ").lower()   
#     letters.append(letter)

# def count_letter_in_text(text, letter):
#     var = text.count(letter)
#     print(f"The letter {letter} appears {var} times")
# count_letter_in_text(text, letters[0])
# count_letter_in_text(text, letters[1])
# count_letter_in_text(text, letters[2])


# letra2 = input("Ingresa la segunda letra: ").lower()
# letra3 = input("Ingresa la tercera letra: ").lower()


# apariciones_letra1 = texto.lower().count(letra1)
# apariciones_letra2 = texto.lower().count(letra2)
# apariciones_letra3 = texto.lower().count(letra3)

# palabras = len(texto.split())

# primera_letra = texto[0]
# ultima_letra = texto[-1]

# palabras_revertidas = " ".join(texto.split()[::-1])

# print(f"La letra '{letra1}' aparece {apariciones_letra1} veces en el texto.")
# print(f"La letra '{letra2}' aparece {apariciones_letra2} veces en el texto.")
# print(f"La letra '{letra3}' aparece {apariciones_letra3} veces en el texto.")
# print(f"El texto tiene {palabras} palabras.")
# print(f"La primera letra del texto es '{primera_letra}'.")
# print(f"La última letra del texto es '{ultima_letra}'.")
# print(f"El texto con las palabras revertidas: {palabras_revertidas}")

# texto = input("Ingrese un Texto: ").lower()

# l1 = input("Digite una letra: ")
# l2 = input("Digite una segunda letra: ")
# l3 = input("Digite una tercera letra: ")

# letras_lista = [l1, l2, l3]

# for letra in letras_lista:
#     cantidad = texto.count(letra)
#     print(f"La letra {letra} aparece {cantidad} veces en el texto.")


# texto_u = input("ingresar texto ")
# letra_u = input("ingrese letra ")
# conteo = texto_u.count(letra_u)
# print = (f"la letra {letra_u} esta {conteo}")


# texto = input("Ingresa un texto: ")


# letra1 = input("Ingresa la primera letra: ").lower()
# letra2 = input("Ingresa la segunda letra: ").lower()
# letra3 = input("Ingresa la tercera letra: ").lower()


# apariciones_letra1 = texto.lower().count(letra1)
# apariciones_letra2 = texto.lower().count(letra2)
# apariciones_letra3 = texto.lower().count(letra3)

# palabras = len(texto.split())


# primera_letra = texto[0]
# ultima_letra = texto[-1]


# palabras_revertidas = " ".join(texto.split()[::-1])


# print(f"La letra '{letra1}' aparece {apariciones_letra1} veces en el texto.")
# print(f"La letra '{letra2}' aparece {apariciones_letra2} veces en el texto.")
# print(f"La letra '{letra3}' aparece {apariciones_letra3} veces en el texto.")
# print(f"El texto tiene {palabras} palabras.")
# print(f"La primera letra del texto es '{primera_letra}'.")
# print(f"La última letra del texto es '{ultima_letra}'.")
# print(f"El texto con las palabras revertidas: {palabras_revertidas}")


contador = 0
contador_L1 = 0
contador_L2 = 0
contador_L3 = 0

cTexto = input("Ingresa un texto (párrafo, frase, poema, etc.) => ")
cLetras = input("Ahora, ingresa tres (3) letras que tú quieras. Importante, separa las letras por un guión (-) => ")

cTexto.lower()
cLetras.lower()

aLetras = cLetras.split("-")
aTexto = list(cTexto)

for i in range(len(aLetras)):
    # Recorro cada una de las letras a buscar
    for n in range(len(aTexto)):
        # comparo y cuento las apariciones
        if aLetras[i] == aTexto[n]:
            contador += 1
    
    if aLetras[i] == aLetras[0]:
        contador_L1 = contador
    elif aLetras[i] == aLetras[1]:
        contador_L2 = contador
    elif aLetras[i] == aLetras[2]:
        contador_L3 = contador

    contador = 0

print(f"La letra '{aLetras[0]}' aparece {contador_L1} veces en el texto, la letra '{aLetras[1]}' aparece {contador_L2} y la letra '{aLetras[2]}' aparece {contador_L3} veces.")