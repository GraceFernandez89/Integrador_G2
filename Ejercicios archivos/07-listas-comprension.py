usuarios = [
    ["Juan", 24],
    ["Sonia", 50],
    ["Lucas", 10]
]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

#Se lo puede escribir de otra manera

#Crear una nueva lista 
# [expresion for item in items]
# nombres = [usuario[0] for usuario in usuarios]

# print(nombres)


#Map
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# print(nombres)


#filter

menos_nombres = list(filter(lambda usuario: usuario[1]>15, usuarios))
print(menos_nombres)