print("---Classificador de Triângulos---")

l1  = int(input("Informe o primeiro lado do triangulo: "))
l2  = int(input("Informe o segundo lado do triangulo: "))
l3  = int(input("Informe o terceiro lado do triangulo: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
     print("O triângulo é EQUILÁTERO.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é ISÓSCELES.") 
    else: 
       print("O triângulo é ESCALENO.")
else:
   print("Os valores informados não formam um triângulo válido.")
    
