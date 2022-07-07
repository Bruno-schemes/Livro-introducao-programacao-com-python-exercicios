# TIPO             FAIXA(KWH)             PREÇO

# RESIDENCIAL     ATÉ 500                 R$ 0,40
#                ACIMA DE 500             R$ 0,65
# 
# COMERCIAL     ATÉ 1000                  R$ 0,55  
#               ACIMA DE 1000             R$ 0,60
# 
# INDUSTRIAL    ATÉ 5000                  R$ 0,55
#               ACIMA DE 5000             R$ 0,60


kwh = int(input("Qual o valor consumido? "))
sala = input("Qual seu tipo espaço? (residencial, comercial ou industrial) ")
r = "residencial"
c = "comercial"
i = "industrial"  

if kwh <= 500 and sala == r:
    print(f"{kwh * 0.40:6.2f} A pagar")

elif kwh > 500 and sala == r:
    print(f"{kwh * 0.65:6.2f} A pagar")  

elif kwh <= 1000 and sala == c:
    print(f"{kwh * 0.55:6.2f} A pagar")

elif kwh > 1000 and sala == c:
    print(f"{kwh * 0.60:6.2f} A pagar")

elif kwh <= 5000 and sala == i:
    print(f"{kwh * 0.55:6.2f} A pagar")  

else:
    print(f"{kwh * 0.60:6.2f} A pagar")          