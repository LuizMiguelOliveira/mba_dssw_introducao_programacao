Valor = float(input("Escreva o valor do Produto: "))
Percent = float(input("Escreva o valor do Desconto: "))

Desconto = (Percent / 100) * Valor
ValorFinal = Valor - Desconto

print(f"O valor do desconto e  de {Desconto:.2f} Reais ")
print(f"O valor do produto final e de {ValorFinal:.2f} Reais ")

