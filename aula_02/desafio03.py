print("----Índice de Massa Corporal----")

name = input("Informe o seu Nome: ")
p = float(input("Informe seu Peso: "))
a = float(input("Informe sua Altura: "))

imc = p / (a ** 2)

if imc < 18.5:
    print(f"Olá {name} voçe esta abaixo do peso. ")
elif imc > 18.5:
    print(f"Olá {name} voçe esta no peso normal. ")
elif imc > 25:
    print(f"Olá {name} voçe esta com sobrepeso. ")
elif imc > 30:
    print(f"Olá {name}voçe esta com Obesidade 1 grau. ")
elif imc > 35:
    print(f"Olá {name}voçe esta com Obesidade 2 grau. ")
elif  imc > 40:
    print (f" Olá {name}voçe esta com Obesidade 3 grau. ")
else:
    print (f"Olá {name}Informe valores corretos")