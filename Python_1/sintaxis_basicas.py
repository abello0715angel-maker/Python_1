
#Introducción a las variables en Python.
#======================================================
nombre = "Bela"  # Variable de tipo string (cadena de texto)
documento = 456   # Variable de tipo int (número entero)
direccion = "Villavicencio"  # Variable de tipo string (cadena de texto)
tiene_deudas = True     # Variable de tipo bool (booleano)

print(documento)

print("="*60)

print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))

print("=="*30)
print("Mi documento es: " ,documento, " y mi direccion es:", direccion)

print("=="*30)
print("\n Concatenación usando F-Strings")
print(f"Mi nombre es {nombre} y mi documento es {documento}")

print("\nMostrar varias variables con F-String")
print(f"""
Numero de Documento = {documento}
Nombre = {nombre}
¿Tiene deudas? = {tiene_deudas}
Dirección= {direccion}
""")
print("==="*29)
print(f"\n ¡Hola {nombre}!")
print(f"Bienvenido a Python {nombre}. \n")