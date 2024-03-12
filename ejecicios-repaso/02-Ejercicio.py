# Nombre = input("Digita tu Nombre: ")
# Ventas = float(input("Cuanto has vendido en este mes: "))

# Comisión = Ventas * 0.13

# print(f"{Nombre} para tus ventas {Ventas} tu comsion es {round(Comisión,2)}")


# nombre = input("Digite su nombre:\n")
# canVentas = float(input("Digite la cantidad vendida en este mes:\n"))
# comision = round((canVentas * 0.13), 2)
#print("Su nombre es: {} y su comision correspondiente es: {}".format(nombre, comision))

# vendedor = input("ingrese el nombre del vendedor: ")
# ventas = float(input("ingrese el valor de las ventas realizadas en el mes: "))
# print(f"el vendedor {vendedor} gano ${round(ventas*0.13,2)} por comisiones del mes")

# nombre = input("Ingrese el nombre del vendedor: ")
# ventas = int(input("Ingrese cunato vendio: "))
# comisiones = round(ventas*0.13,2)
# print(f"{nombre} vendio {ventas} pesos y su comision es de {comisiones}pesos")

# nombre = input("Ingresar el nombre del empleado")
# ventas=float(input("ingrese las ventas de este mes"))
# ventas_totales = (ventas * 13)/100
# print("El nombre del empleado es",nombre, "y sus ventas totales fueron",ventas_totales)


# def calcular(total):
#     r=total * 0.13
#     return round(r,2)
# if __name__ == "__main__":
#     n = input("escribe tu nombre ")
#     t = float(input("escrbe tus ventas del mes "))
#     c = calcular(t)
#     print(f"vendedor (a) {n} su comisión es {c}")


# def calc(total):
#     r=total * 0.13
#     return round(r,2)


# nom = input("escribe tu nombre ")
# total = float(input("escrbe tus ventas del mes "))
# sum = calc(total)
# print(f"vendedor {nom} su comisión es {sum}")


# print("***Programa: Calcula comisiones ****")
# cNombre =input("Cuales tu nombre? => ")
# nTotal_Ventas = float(input("Cual es el total de tus ventas al mes? => "))

# nComision = round(nTotal_Ventas*13/100,2)

# print(f"{cNombre} :Tu comisión mensual es de -> {nComision} pesos")


# nombre= input("ingresa nombre")
# ventas_totales = float(input("ingresa el monto total de tus ventas"))


# calculo = ventas_totales*0.13
# calculor = round(calculo,2)
# print(f" {nombre }tus ganancias de este mes fue {calculor}")

# nombre = input("ingresa tu nombre->")
# ventas = float(input("Ingresa numero de ventas->"))
# bonificacion = ventas * 0.13
# print(f"{nombre} tus ventas fueron {ventas} y tu comision es {round(bonificacion,2)}")

# nombre = input("Ingresa tu nombre: ")
# venta = float(input("Ingresa el total de la venta: "))
# comision = round(venta * 13) / 100
# print(f"{nombre}, tu comisión por la venta es: {comision}")

# nombre = input("Ingrese su nombre: ")
# ventas = float(input("Ingrese sus ventas de este mes: "))
# comision = round((ventas*0.13), 2)
# print(f"{nombre} ha vendido {ventas} pesos y su comision es de {comision}pesos")


# name =input("What's your name: ")
# total_sale = input("What's your total sale: ")
# value = float(total_sale)
# comision = round((value * 13/100),2)
# print(f"The comision value to : {name} is {comision}")


# nombre = input("¿Cuál es tu nombre? ")
# ventas_totales = float(input(f"Hola {nombre}, ¿cuánto has vendido este mes? "))
# comision = ventas_totales * 0.13
# print(f"{nombre}, tu comisión este mes es de ${comision:.2f}.")


# nombre = input("Ingresar el nombre del empleado")
# ventas=float(input("ingrese las ventas de este mes"))
# ventas_totales = (ventas * 13)/100
# print("El nombre del empleado es",nombre, "y sus ventas totales fueron",round(ventas_totales))


# nombre = input("Ingrese el Nombre del Empleado: ")
# ventas = float(input("Ingrese el Valor de Ventas del mes :" )) 
# porcentaje = round(ventas * 0.13,2)
# print(f"Señor: {nombre} El Valor total de su Comisión es: {porcentaje}")


# def get_información_usuario():
#     nombre = input("Por favor, ingrese su nombre: ")
#     monto = float(input("Por favor, ingrese el monto de la venta: "))
#     return nombre, monto
# def calcular_porcentaje(monto):
#      return round(monto * 0.13, 2)
# def print_result(nombre, porcentaje):
#     print(f"La bonificación de ventas de {nombre} es: {porcentaje}")
# def main():
#     nombre, monto = get_información_usuario()
#     porcentaje = calcular_porcentaje(monto)
#     print_result(nombre, porcentaje)
# main()


# Nombre=input("nombre del vendedor:")
# ventas=float(input("ingrese las ventas realizadas este mes:"))
# comision=round(ventas*13/100,2)
# print(f"vendedor:{Nombre},comision mensual:{comision}")


nombre_vendedor = input("ingrese nombre vendedor: ")
comision_vendedor = float(input("ingresos: "))
operacion = round((comision_vendedor * 13)/100)
print(f"nombre vendedor {nombre_vendedor} total de su Comisión es: {operacion}")