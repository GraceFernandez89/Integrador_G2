# #Sobreescribir un archivo existente
# archivo = open('prueba2.txt', 'w')
# archivo.write('Soy el nuevo texto')
# archivo.close()

# #Crear o escribir un nuevo archivo
# archivo = open('prueba3.txt', 'w')
# archivo.write('Soy el nuevo texto')
# archivo.close()


#Al crear una nueva linea se puede observar que las lineas que se agregan
#no contienen un salto de linea
# archivo = open('prueba2.txt', 'w')
# archivo.write('Soy el nuevo texto')
# archivo.write('Hola mundo')
# archivo.close()

# #Se puede agregar un salto de linea
# archivo = open('prueba2.txt', 'w')
# archivo.write('Soy el nuevo texto\n')
# archivo.write('Hola mundo')
# archivo.close()


#Se puede agregar un salto de linea
# archivo = open('prueba2.txt', 'w')
# archivo.write('''Soy el nuevo texto 
# hola mundo
# aqui estoy''')

# archivo.close()


###############################################
#writelines con este metodo se crea una lista de strings
 

# archivo = open('prueba4.txt', 'w')
# archivo.writelines(['hola','mundo','aqui','estoy'])

# archivo.close()

######################################################

# archivo = open('prueba5.txt', 'w')
# lista = ['hola','mundo','aqui','estoy']

# for p in lista:
#     archivo.writelines(p + '\n')
# archivo.close()

#######################################################
#Abre el archivo lleva el cursor hasta el final del texto que 
# que contenga y desde ahi va a comenzar a escribir 

archivo = open('prueba3.txt', 'a')

archivo.write('Bienvenido')


archivo.close()