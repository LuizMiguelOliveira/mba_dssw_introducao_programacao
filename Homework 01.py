
bemvindo = "Bem-Vindo a Calculadora Espacial"
print(bemvindo)

planeta_o = input("Informe o nome do Planeta de Origem: ")
planeta_d = input("Informe o Nome do Planeta de Destino: ")
distancia = float(input("Informe a Distância entre esses planetas (em milhões de KM): "))
velocidade_n = float(input("Informe a velocidade da nave (em mil km/h): "))

tempo = distancia / velocidade_n
dias = tempo / 24

print(f"O Planeta de Origem é {planeta_o} e o Planeta de Destino é {planeta_d}")
print(f"O tempo que levará para chegar no Planeta {planeta_d} é de {tempo:.2f} Horas ou {dias:.2f} Dias.")



