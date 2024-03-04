from pathlib import Path

#carpeta = Path('E:/GRACE/docente/28-02-2024/carpeta1')
# carpeta = Path('/GRACE/docente/28-02-2024/carpeta1')
# #Concatenacion para rutas 
# archivo = carpeta / 'otro_archivo.txt'

# mi_archivo = open(archivo)
# print(mi_archivo.read())

#Cual quier usuario puede abrir este archivo con este codigo

#######################################################################
#Funcionalidad de pathlib
#No se necesita el close ni el open

carpeta = Path('E:/GRACE/docente/28-02-2024/carpeta1/otro_archivo.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)#la extension
print(carpeta.stem)#Nombre del archivo sin la extension



