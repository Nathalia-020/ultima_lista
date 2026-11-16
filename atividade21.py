#21\. O Chapéu Seletor Clássico
#Faça a pergunta: "Você prefere: 1-Livros, 2-Esportes, 3-Natureza, 4-Pegadinhas". Use if/elif/else para sortear o aluno em uma das 4 casas da escola de magia (ex: Corvinal, Grifinória, Lufa-Lufa, Sonserina).

print("Você prefere:") 
print("1 - Livros") 
print("2 - Esportes") 
print("3 - Natureza") 
print("4 - Pegadinhas")

escolha = int(input("Digite sua escolha: "))

if escolha == 1: 
    print("Você pertence à Corvinal!")

elif escolha == 2: 
    print("Você pertence à Grifinória!")

elif escolha == 3: 
    print("Você pertence à Lufa-Lufa!")

elif escolha == 4: 
    print("Você pertence à Sonserina!")

else: 
    print("Escolha inválida!")

