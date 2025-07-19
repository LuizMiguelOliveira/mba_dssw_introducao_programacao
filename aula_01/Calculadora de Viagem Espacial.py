planeta_o = input("Informe o nome do Planeta de Origem: ")
planeta_d = input("Informe o Nome do Planeta de Destino: ")
distancia = float(input ("Informe a Distancia entre esses planetas (em milhões de KM): "))
velocidade_n = float(input ("informe a velocidade da nave ( em mil km/h): "))

tempo = distancia / velocidade_n
dias = tempo / 24

print (f"O Planeta de Origem e {planeta_o} e o Planeta de Destino e {planeta_d}")
print (f"O tempo que levará para chegar no Planeta {planeta_d} e de {tempo:.2f} Horas ou `{dias:.2f} Dias. ")