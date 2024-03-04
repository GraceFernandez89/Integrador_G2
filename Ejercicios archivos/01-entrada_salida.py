#Primero este ejemplo
#Trasfiero a la variable mi archivo el contenido de prueba.txt
mi_archivo = open('prueba.txt')
#Libreria utilizada io
# print(mi_archivo)

# #Leer archivo
# print(mi_archivo.read())


################################################################################
#Leer una linea (readline)
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")

#Quitar el salto de linea 
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea.rstrip()}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")

#Como es un cadena tenemos todos los metodos para aplicar a las cadenas

# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea.upper()}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea.lower()}")
# una_linea = mi_archivo.readline()
# print(f"esta es la linea {una_linea}")


#Se puede iterar las lineas de un archivo

# for l in mi_archivo:
#     print("Aqui dice: " + l)

#################################################################################

#readlines

todas_lineas = mi_archivo.readlines()
print(todas_lineas)#Lista y se puede aplicar todos los metodos de una lista

todas_lineas = todas_lineas.pop()
print(todas_lineas)








#Se debe cerrar esta conexion del open
mi_archivo.close()

