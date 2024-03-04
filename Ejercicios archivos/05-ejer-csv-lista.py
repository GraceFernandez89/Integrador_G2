import csv

# contactos = [
#     ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
#     ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
#     ("Javier", "Analista de datos", "javier@ejemplo.com"),
#     ("Marta", "Experta en Python", "marta@ejemplo.com")
# ]


#Escritura de listas en CSV


#Permite abrir un fichero dentro de un bloque de codigo y no hace falta que lo cerremos manualmente
#newline especifica el caracter de salto de linea que queremos 
# csvfile nombre de la variable que abrita el fichero
# with open("contactos.csv", "w", newline="\n") as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     for contacto in contactos:
#         writer.writerow(contacto)
        

#Lectura de listas en CSV


with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)        
        
        
