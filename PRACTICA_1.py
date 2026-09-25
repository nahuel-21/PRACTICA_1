# TAREA 1
A = set(input("Elementos de A: ").split(","))
B = set(input("Elementos de B: ").split(","))

print("Elementos en A, B o ambos:", A | B )

x = input("Ingreses un elemento: ")

if x in A and x in B:
    print("Está en ambos conjuntos")
elif x in A:
    print("Está en A")
elif x in B:
    print("Está en B")
else:
    print("No está en ninguno")



A = set(input("Elementos de A: ").split(", "))
B = set(input("Elementos de B: ").split(", "))

print("Elementos en A o en B, o en ambos:", A | B)

x = input("Ingrese un elemento: ")

if x in A and x in B:
    print("Está en ambos conjuntos")
elif x in A:
    print("Está en A")
elif x in B:
    print("Está en B")
else:
    print("No está en ninguno")

A = set(input("Elementos de A: ").split(", "))
B = set(input("Elementos de B: ").split(", "))

print("Elementos en A o en B, pero no en ambos:", A ^ B)

A = set(input("Elementos de A: ").split(", "))
B = set(input("Elementos de B: ").split(", "))

if A <= B:
    print("A es subconjunto de B")
else:
    print("A no es subconjunto de B")

A = set(input("Elementos de A: ").split(", "))

print("El conjunto A tiene", len(A), "elementos")
