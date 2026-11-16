#17\. A Feira de Poções Múltiplos Produtos
# Mostre um menu com 3 poções e preços diferentes. Peça para o usuário digitar 1, 2 ou 3. Use if/elif/else para calcular o valor da compra baseado na escolha.
print("=== FEIRA DE POÇÕES ===") 
print("1 - Poção de Cura: R$ 10") 
print("2 - Poção de Força: R$ 15") 
print("3 - Poção Mágica: R$ 20")

escolha = int(input("Digite sua escolha: "))

if escolha == 1: 
    print("Você comprou a Poção de Cura.") 
    print("Total: R$ 10")

elif escolha == 2: 
    print("Você comprou a Poção de Força.") 
    print("Total: R$ 15")

elif escolha == 3:
    print("Você comprou a Poção Mágica.")
    print("Total: R$ 20")
 
else:
    print("Opção inválida!")
