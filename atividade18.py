#18\. Imposto do Reino
#Peça o valor do tesouro do herói. Se o tesouro for maior que 1000 moedas, o rei cobra uma taxa de 10% (calcule a matemática e mostre o desconto). Se for menor ou igual a 1000, o herói não paga imposto.

tesouro = float(input("Digite o valor do tesouro: "))

if tesouro > 1000: 
    imposto = tesouro * 0.10 
    total = tesouro - imposto 
    print("Imposto de 10%:", imposto) 
    print("Valor final:", total)

else:
    print("Você não paga imposto!") 
    print("Valor final:", tesouro)

