valor_brl = float(input("Digite o valor em Reais (BRL): "))

taxa_cambio = 5.0

valor_usd = valor_brl / taxa_cambio

print(f"R$ {valor_brl:.2f} e a mesma coisa que US${valor_usd:.2f}")