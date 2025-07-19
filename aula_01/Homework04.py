print(" Bem - Vindo a calculadora de IMC")

nome = input(" Informe o seu nome: ")
peso = float(input(" Informe o seu peso(KG): "))
altura = float(input(" Informe a sua altura: "))

imc = peso / (altura * altura)

print(F" {nome} seu IMC é de: {imc:.2f}")