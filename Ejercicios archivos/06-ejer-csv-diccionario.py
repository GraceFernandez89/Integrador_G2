        
import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

# with open("contactos2.csv", "w", newline="\n") as csvfile:
#     campos = ["nombre", "empleo", "email"]
#     writer = csv.DictWriter(csvfile, fieldnames=campos)
#     writer.writeheader()
#     for nombre, empleo, email in contactos:
#         writer.writerow({
#             "nombre": nombre, "empleo": empleo, "email": email
#         })        
        
        
with open("contactos2.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])        