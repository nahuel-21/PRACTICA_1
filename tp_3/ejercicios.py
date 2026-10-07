
# --- ejercicio 1 ---

def ejercicio_1():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    mayor = num1 if num1 > num2 else num2

    print(f"El mayor es: {mayor:g}")

# --- ejercicio 2 ---
def buscar_palabra(palabra_buscada, *palabras):
    return "Palabra encontrada" if palabra_buscada in palabras else "Palabra no encontrada"

def ejercicio_2():

    lista = []

    print("Ingrese las palabras de la lista (escriba 'fin' para terminar):")
    while True:
        palabra = input("Palabra: ")
        if palabra == "fin":
            break
        lista.append(palabra)

    print("Lista guardada:", lista)

    buscada = input("Ingrese la palabra a buscar: ")
    print(buscar_palabra(buscada, *lista))

# ---ejercicio 3 ---
def ejercicio_3():

    numero = int(input("Ingrese un número: "))

    resultado = "Es par" if numero % 2 == 0 else "Es impar"

    print(resultado)

# ---ejercio 4---

def calcular_promedio(*numeros):
    return sum(numeros) / len(numeros) if len(numeros) > 0 else 0

def ejercicio_4():

    lista = []

    print("Ingrese los números de la lista (escriba 'fin' para terminar):")
    while True:
        dato = input("Número: ")
        if dato == "fin":
            break
        lista.append(float(dato))

    print("Lista guardada:", lista)

    promedio = calcular_promedio(*lista)
    print(f"El promedio es: {promedio:g}")


# --- ejercios 5 ---
def sumar(*numeros):
    minimo = 5
    return f"La suma es: {sum(numeros):g}" if len(numeros) >= minimo else f"Error: se necesitan al menos {minimo} argumentos y se pasaron {len(numeros)}"

def ejercicio_5():

    lista = []

    print("Ingrese los números (escriba 'fin' para terminar):")
    while True:
        dato = input("Número: ")
        if dato == "fin":
            break
        lista.append(float(dato))

    print(sumar(*lista))

# -- ejerciciso ---
ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]


for i, ejercicio in enumerate(ejercicios, start=1):
    print(f"\n===== EJERCICIO {i} =====")
    ejercicio()
    if i < len(ejercicios):
        input("\nPresione Enter para pasar al siguiente ejercicio...")

print("\n===== FIN DE LA PRÁCTICA =====")