
"""
#Ejercicio 1: Mostrar la tabla de multiplicar de un número.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range (1, 11):
    print(f"{numero} x {i} = {numero*i} ")
"""

"""
#Ejercicio 2: Sumar los primeros números n naturales.
n=int(input("Ingrese un número natural: "))
suma=0
for i in range (1, n+1):
    suma= suma + i
print(f"La suma de los primeros {n} números naturales es: {suma}")
"""
"""
#Ejercicio 3:  Contar cuántos números pares hay entre 1 y n.
n=int(input("Ingrese un número natural: "))
contador= 0
numero = 1
while numero <=n:
    if numero % 2 == 0:
        contador= contador + 1
    numero= numero + 1
print(f"Hay {contador} números pares entre 1 y {n}.")
"""
"""
#Ejercicio 4: Solicitar una contraseña hasta que sea correcta.
clave_correcta = "Python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo.")
    clave_ingresada=input(("Ingrese la contraseña: "))

print("Contraseña correcta, acceso concedido.")
"""

"""#Ejercicio 5: Calcular el factorial de un número.
n= int(input("Ingrese un número natural: "))
factorial= 1
for i in range (1, n+1):
    factorial= factorial * i
print(f"El factorial de {n} es {factorial}.")
"""

#Taller 3: Ejercicios para resolver.

"""
#Adivinar el número.
 import random
numero= random.randint(1, 10)
intentos=0

while intentos <3:
    intento=int(input("Adivina el número (1, 10): "))

    if intento <0 or intento >10:
        print(f"El número {intento} no es válido. Intenta de nuevo.")
        continue
    
    intentos= intentos + 1
    print(f"Intento {intentos}.")

    if intento==numero:
        print("¡Correcto, acertaste!")
        break
else:
    print(f"Perdiste, el número era: {numero}.")
"""

"""
#Cuenta regresiva.
num_inicial= int(input("Ingrese el valor para iniciar la cuenta regresiva:"))

if num_inicial >0:
    while num_inicial >=0:
        print(f"{num_inicial}")
        num_inicial= num_inicial - 1
    print("La cuenta ha finalizado.")
else:
    print(f"El número {num_inicial} es inválido.")
"""

"""
#Números Impares.
for i in range (1, 101):
    if i % 2 == 1:
        print(i)
"""

"""
import datetime

while True:
    print("1) Mensaje de bienvenida.")
    print("2) Fecha y hora actual.")
    print("3) Salir del programa.")

    opcion= int(input("Seleccioen una opción: "))

    if opcion == 1:
        print("¡Bienvenido al programa de Angel!")
    elif opcion == 2:
        print(datetime.datetime.now())
    elif opcion == 3:
        break
    else:
        print("Opción inválida.")
"""

"""
#Registro de notas y  cálculo del promedio.
num_notas= int(input("Ingrese la cantidad de notas: "))
suma_notas= 0

for i in range(num_notas):
    nota = float(input("Ingrese una nota: "))
    suma_notas= suma_notas + nota
promedio= suma_notas/num_notas
if promedio >=3:
    print(f"Tu promedio es {promedio} y aprobaste.")
else:
    print(f"Tu promedio es {promedio} y desaprobaste.")
"""

"""
num = int(input("Ingrese un número natural: "))
suma= 0
if num >0:
    suma=0
    for i in range (1, num+1):
        if i % 2 ==0:
            suma= suma + i
    print(suma)

else:
    print("El número es inválido.")
"""

"""
n = int(input("Ingrese un número: "))

while n >=0:
    print(n)
    n= n-1
"""

"""
while True:
    num=int(input("Ingrese un número:"))
    if num <0:
        print("Número Inválido.")
    elif num >0:
        print("Número Válido.")
    else:
        print("Programa Terminado.")
        break
"""

"""
num= int(input("Ingrese un número natural: "))
num_impar= 0

for i in range (1, num + 1):
    if i % 2 == 1:
        num_impar= num_impar + 1
print(f"Cantidad de impares: {num_impar}.")
"""

"""
num= int(input("Ingrese un número natural: "))
multiplos= 0

if num >0:
    for i in range (1, num + 1):
        if i % 3 == 0:
            print(i)
            multiplos= multiplos + 1
    print(f"Hay {multiplos} multiplos de 3 desde el 1 hasta el {num}.")
else:
    print("Número inválido.")
"""
"""
num= int(input("Ingrese un número natural: "))
suma= 0

if num>0:
    for i in range (1, num + 1):
        if i % 2 ==0:
            print(i)
            suma= suma + i
    print(f"La suma de los números pares del 1 hasta el {num} es {suma}. ")
else:
    print("Número inválido.")
"""

"""
num= int(input("Ingrese un número natural: "))
multiplos= 0
suma= 0

if num>0:
    for i in range (1, num+1):
        if i % 5==0:
            print(i)
            multiplos= multiplos + 1
            suma= suma + i
    print(f"Cantidad de múltiplos de 5: {multiplos}.")
    print(f"La suma de los múltiplos de 5, desde el 1 hasta el {num} es {suma}")
else:
    print("Número inválido.")
"""
