import subprocess
import os

def limpiar():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
def cargar_numero():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input ("ingrese segundo numero: "))
    return num1, num2

#ejercicio 1
def dividir(a , b):
    try:
        resultado = a / b
        print(f"Resultado: {a} / {b} = {resultado}" )
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")

#ejercicio 2
def sumar_numero_y_cadena(numero, cadena):
    try:
        resultado = numero + cadena
        print(f"Resultado: {resultado}")
    except TypeError:
        print("Error: no se puede sumar un nemero y una cadena de texto")

#ejercicio 3
def buscar_en_diccionario(diccionario, clave):
    try:
        valor = diccionario[clave]
        print(f"El valor de '{clave}' es: {valor}")
    except KeyError:
        print(f"Error: la clave '{clave}' no existe en el diccionario")

#ejercicio 4
def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"El archivo '{nombre_archivo}' existe. Contenido:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe")
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Archivo creado automáticamente por el programa.")
        print(f"Se creó el archivo '{nombre_archivo}'")

#ejercicio 5
def dividir_con_validacion(texto1, texto2):
    try:
        a = float(texto1)
        b = float(texto2)
        resultado = a / b
        print(f"Resultado: {a} / {b} = {resultado}")
    except ValueError:
        print("Error: debe ingresar un número válido")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")



limpiar()
num1, num2 = cargar_numero()

while True:
    print("====Ejercicios====")
    print("1- Ej 1")
    print("2- Ej 2")
    print("3- Ej 3")
    print("4- Ej 4")
    print("5- Ej 5")
    print("0- SALIR")
    opcion = input("Elije un ejercicio: ")

    limpiar()

    if opcion == "1":
        print ("===Ejercicio 1===")
        dividir(num1, num2)
    elif opcion == "2":
        print("--- Ejercicio 2 ---")
        texto = input("Ingrese un texto: ")
        sumar_numero_y_cadena(num1, texto)
    elif opcion == "3":
        print ("===Ejercicio 3===")
        alumno = {"nombre": "Juan", "edad": 20, "curso": "Python"}
        print(f"Claves disponibles: {list(alumno.keys())}")
        clave = input("Ingrese la clave que desea buscar: ")
        buscar_en_diccionario(alumno, clave)
    elif opcion == "4":
        print ("===Ejercicio 4===")
        nombre = input("Ingrese el nombre del archivo (ej: datos.txt): ")
        abrir_archivo(nombre)
    elif opcion == "5":
        print ("===Ejercicio 5===")
        texto1 = input("Ingrese el primer número: ")
        texto2 = input("Ingrese el segundo número: ")
        dividir_con_validacion(texto1, texto2)
    elif opcion == "0":
        print("programa finalizado")
        break
    else:
        print("Opcion invalida, intente nuevamente.")
