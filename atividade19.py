#19\. Caixa Eletrônico da Mesada
#O pai deu a mesada, mas perguntou: "Você tirou nota A em matemática?". Se a resposta for "sim", a mesada recebe um bônus de 20 moedas. Se for "não", recebe apenas o valor normal. Imprima o total final.

mesada = float(input("Digite o valor da mesada: "))

resposta = input("Você tirou nota A em matemática? ")

if resposta == "sim": total = mesada + 20

else: total = mesada

print("Sua mesada final é:", total)

