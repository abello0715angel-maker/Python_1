
numero1= 14
numero2=5
suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

print(f"""
suma            = {numero1} + {numero2} = {suma}
resta           = {numero1} - {numero2 } = {resta}
multiplicacion  = {numero1} * {numero2} = {multiplicacion}
division        = {numero1} / {numero2} = {division:.6f}
resto           = {numero1} // {numero2} = {resto}
potencia        = {numero1} ** {numero2} = {potencia}
""")


"""
print("=="*30)
#Ejercicio 1 : Suma de dos números.
numero3 = float(input("Ingrese el primer número : "))
numero4 = float(input("Ingrese el segundo número : "))
suma2= numero3 + numero4
print(f"La suma es {suma2}.")
print("=="*30)
"""

"""
#Ejercicio 2 : Área de un rectángulo.
base = float(input("Ingrese la medida de la base : "))
altura = float(input("Ingrese la medida de la altura : "))
area = base * altura
print(f"El área del rectángulo es {area}.")
print("=="*30)
"""

"""#Ejercicio 3 : Conversión de minutos a horas y minutos.
minutos_totales = int(input("Ingrese la cantidad de minutos : "))
horas= minutos_totales // 60
minutos= minutos_totales% 60 
print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos.")
print("=="*30)
"""

"""
#Ejercicio 4: Cálculo del precio con descuento.
precio=float(input("Ingrese el precio del producto : "))
descuento=float(input("Ingrese el porcentaje del descuento: "))
valor_descuento = precio * (descuento/100)
precio_final= precio - valor_descuento

print(f"El precio final a pagar es {precio_final}.")
print("=="*32)
"""

"""
#Ejercicio 5: Intercambio de valores entres dos variables.
a = float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
auxiliar=a
a=b
b=auxiliar
print(f"Después del intercambio a={a} y b={b}.")
print("=="*30)
"""

#Taller 1 : Ejercicios para resolver.

"""
#Perímetro de un terreno rectangular.
largo=float(input("Ingrese el valor del largo del terreno: "))
ancho=float(input("Ingrese el valor del ancho del terreno: "))
print(f"El perímetro del terreno es {(largo + ancho)*2}.")
"""
"""
#Promedio de valores.
numero3=float(input("Ingrese el valor del primer número: "))
numero4=float(input("Ingrese el valor del segundo número: "))
numero5=float(input("Ingrese el valor del último número: "))
print(f"El promedio es {(numero3+numero4+numero5)/3}.")
"""

"""
#Nombre y edad.
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
print(f"Hola, soy {nombre} y tengo {edad} años.")
"""
"""
#COP a USD
cop=int(input("Ingrese la cantidad de pesos colombianos a cambiar: "))
print(f"Sus {cop} pesos colombianos son equivalentes a {cop/4000} dólares.")
"""

"""
#Segundos a Horas,Minutos y Segundos.
segundos=int(input("Ingrese la cantidad de segundos: "))
horas= segundos // 3600
segundos_restantes= segundos%3600
minutos= segundos_restantes//60
segundos_finales=segundos_restantes%60

print(F"{segundos} segundos son {horas} horas,{minutos} minutos y {segundos_finales} segundos.")
"""
