#Ejercicio 1: try/except básico

"""try:
    numero= int(input("Ingrese un número: "))
    print(f"El número ingresado es {numero}.")
except ValueError:
    print("Error: debe ingresar un número entero válido.")
"""
"""
#Ejercicio 2: División segura con ZeroDivisionError
try:
    dividendo= float(input("Ingrese el dividendo: "))
    divisor= float(input("Ingrese el divisor: "))
    resultado= dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre 0")
except ValueError:
    print("Ingrese solo valores númericos.")
"""
"""
#Ejercicio 3: else y finally
try:
    edad= int(input("Ingrese su edad: "))
except ValueError:
    print("Error: La edad debe ser un número entero.")
else:
    if edad>=18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")

"""