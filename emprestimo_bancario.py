casa = int(input("Qual o valor da casa que deseja financiar? "))
salario = int(input("Qual seu salario? "))
qtd = int(input("Em quantas x pretende pagar? "))

vezes = casa / qtd  #divido o valor da casa pela quantidade de parcelas.
porc = salario * 0.30 # 30% do salario.

if vezes <= porc: # se o valor da casa dividido pela quantidade de parcelas for menor ou igual a 30% do salario, é aprovado o financiamento.
    print("Parabéns, seu financiamento foi aprovado!!")
    
else:
    print("Infelizmente não foi possivel efetuar o financiamento.")
   

