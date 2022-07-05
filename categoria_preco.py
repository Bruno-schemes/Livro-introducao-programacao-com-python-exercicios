categoria = int(input("Digite a categoria do produto de 1/5: ")) # digte um numero de 1 a 5 denpendendo do numero um if irá responder

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18  
elif categoria == 3:
    preço = 23     
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
     print("Produto invalido ou indisponivel")
     preço = 0     
print(f"O preço do produto é: R${preço:6.2f}")                               