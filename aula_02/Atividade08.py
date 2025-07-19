print (" ---- Comparador de Números ----")

p1 = int(input(" Informe o Primeiro Número: "))
p2 = int(input(" Informe o Segundo Número: "))

if p1 > p2:
    print(f"`{p1} e maior que o valor {p2}")
elif p2 > p1:
    print(f"`{p2} e maior que o valor {p1}")
else:
    print("Informe um valor aceitavel")
