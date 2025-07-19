print("----Conversor de Temperatura----")

temp = float(input(" Digite a temperatuda: "))
escala = input("Informe a escala de origem (C para Celsius ou F para Fahrenheit):").upper()

if escala == "C":
     f = (temp * 9/5) + 32
     print(f"{temp:.2f}°C equivalente a {f:.2f}°F")
elif escala == "F":
     c = (temp - 32) * 5/9
     print(f"{temp:.2f}°F equivalente a {c:.2f}°C")
else:
     print("Escala Invalidada: Informe 'C' para celcius e 'f' para fahrenheit")