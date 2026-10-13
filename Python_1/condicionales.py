
"""
#Ejercicio 1: Determinar si un número es positivo, negativo o cero.

numero=float(input("Ingrese un número: "))

if numero >0:
    print(f"{numero} es positivo.")
elif numero <0:
    print(f"{numero} es negativo.")
else:
    print(f"{numero} es nulo.")
"""

"""
#Ejercicio 2: Verificar si una persona es mayor de edad.
edad=int(input("Ingrese su edad actual: "))

if edad <0:
    print("Error: Edad negativa. Vuelve a intentarlo.")
elif edad >=18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
"""

"""
#Ejercicio 3: Determinar si un número es par o impar.
numero=int(input("Ingrese un número entero: "))

if numero %2 ==0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
"""

"""#Ejercicio 4: Asignar una nota académica.
nota=float(input("Ingrese su nota: "))
if nota <0:
    print("Error: Nota ne permitida.")
elif nota >5:
    print("Error: Nota no permitida.")
elif nota >=4.5:
    print("Desempeño superior.")
elif nota >=3.5:
    print("Desempeño alto.")
elif nota >=3.0:
    print("Desempeño básico.")
else:
    print("Desempeño bajo.")
"""

"""#Ejercicio 5: Determinar el mayor de tres números.
n1= float(input("Ingrese un número: "))
n2= float(input("Ingrese el segundo número: "))
n3=float(input("Ingrese el último número: "))

if n1 >= n2 and n1>=n3:
    print(f"El número {n1} es el mayor.")
elif n2>=n1 and n2>=n3:
    print(f"El número {n2} es el mayor.")
else:
    print(f"El número {n3} es el mayor.")
"""

"""#Taller 2 : Ejercicios para resolver.

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

if edad <0:
    print(f"La edad {edad} no es válida.")
elif edad >=18:
    print(f"Hola {nombre}, eres mayor de edad.")
else:
    print(f"Hola {nombre}, te faltan {18-edad} años para poder ingresar. ")
"""

"""nombre=input("Ingrese su nombre: ")
nota=float(input("Ingrese su nota: "))

if nota >5:
    print(f"{nota} es inválida.")
elif nota <0:
    print(f"{nota} es inválida.")
else:
    if nota >=3:
        estado= "aprobado."
    else:
        estado= "desaprobado."

    if nota >=4.5:
        desempeño= "desempeño es excelente."
    elif nota >=3.5:
        desempeño= "desempeño es bueno."
    elif nota >=3:
        desempeño= "desempeño es aceptable."
    else:
        desempeño= "desempeño es insuficiente."

    print(f"Hola {nombre} tu nota final es {nota}, estás {estado} y tu {desempeño}")
"""

"""
nombre=input("Ingrese su nombre: ")
precio=int(input("Ingrese el valor total de su compra: "))

if precio <0:
    print("El valor ingresado es inválido.")
else:
    if precio <100000:
        porcentaje=0
        descuento=0
        total = precio - descuento
    elif precio <300000:
        porcentaje= 10
        descuento= precio * 0.1
        total = precio - descuento
    elif precio <500000:
          porcentaje= 15
          descuento= precio * 0.15
          total= precio - descuento
    else:
            porcentaje= 20
            descuento= precio * 0.2
            total= precio - descuento
print(f"Hola {nombre}, el valor de su compra es {precio}, su porcentaje de descuento es {porcentaje}% descontando así {descuento} y su total a pagar es {total} pesos.¡Vuelve pronto!")
"""

"""ciudad= input("Ingrese el nombre de la ciudad: ")
temperatura= int(input("Ingrese la temperatura actual en grados Celcius: "))

if temperatura <10:
    clasififcacion= "muy fría"
    recomendacion= "llevar abrigo"
elif temperatura <=17:
    clasififcacion="fría"
    recomendacion= "llevar abrigo"
elif temperatura <=25:
    clasififcacion= "templada"
    recomendacion= "usar ropa ligera"
elif temperatura <=32:
    clasififcacion= "caliente"
    recomendacion= "mantenerse hidratado"
else:
    clasififcacion="Muy caliente"
    recomendacion="mantenerse hidratado y aplicar protector solar"
print(f"En {ciudad} la temperatura es {temperatura}°C, estando {clasififcacion} y se recomienda {recomendacion}.")
"""
"""
nombre=input("Empleado: ")
horas= int(input("Ingrese la cantidad de horas trabajadas este mes: "))
tarifa= float(input("Ingrese el valor por hora trabajada: "))
horas_extra= (horas-160)
salario_neto= horas*tarifa-(horas*tarifa*0.08)

if horas <0:
    print("Error: Horas inválidas.")
elif tarifa <0:
    print("Error: Tarifa inválida.")
else:
    if horas <=160:
        horas_extra=0
        salario_bruto= horas * tarifa
    elif horas >160:
        salario_bruto= ((horas_extra)*1.25*tarifa)+(160*tarifa)
        print(f"Hola {nombre}, este mes trabajaste {horas} horas, con {horas_extra} horas extra, se te paga por cada hora normal {tarifa} y por cada hora extra {tarifa*1.25} logrando así {salario_bruto}, pero aplicando el descuento de salud y pensión, te queda en {salario_neto}.")
"""
