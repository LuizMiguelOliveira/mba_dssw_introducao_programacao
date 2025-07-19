print("---Inicio do Comando---")

idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA: ") .upper()

if idade >= 18 and ingresso == "vip".upper():
 print("Siga para o primeiro andar!")

elif idade >= 18 and ingresso == "pista".upper():
    print("Siga em frente para ir para pista")

else:
 print("E hora de voltar para casa! ")

print("---Final do Comando---")