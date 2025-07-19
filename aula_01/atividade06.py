import math

PI = 3.14
a = float(input("informe a Altura: "))
r = float(input("Informe o Raio: "))

area_lateral = 2 * PI * a * r
base = PI * (r ** 2)
area_cilindro = area_lateral + base
qtd_litros = area_cilindro / 3
qtd_latas = math.ceil(qtd_litros / 5)
custo_total = qtd_latas * 50

print(f'O custo total da píntura e R${custo_total:2f}')