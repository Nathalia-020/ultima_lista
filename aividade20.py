#20\. A Cantina Inflacionada
#Crie um sistema onde o usuário informa o dinheiro que tem e escolhe Lanche (R$ 15), Suco (R$ 8) ou Combo (R$ 20). O sistema deve usar o elif para identificar a escolha, verificar se o dinheiro dá para pagar, e liberar ou negar a venda.

dinheiro = float(input("Quanto dinheiro você tem? "))

print("1 - Lanche: R$ 15") 
print("2 - Suco: R$ 8") 
print("3 - Combo: R$ 20")

escolha = int(input("Escolha uma opção: "))

if escolha == 1: preco = 15

elif escolha == 2: preco = 8

elif escolha == 3: preco = 20

else: preco = 0 
print("Opção inválida!")

if preco > 0: 
    if dinheiro >= preco: print("Compra autorizada!") 
    print("Troco:", dinheiro - preco)

else:  print("Dinheiro insuficiente!")

