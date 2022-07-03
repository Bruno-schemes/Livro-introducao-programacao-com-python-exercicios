numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite mais um numero: "))
numero3 = int(input("Digite um outro numero: "))


# numeros maiores 

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o numero maior")



if numero2 > numero1 and numero2 > numero3:
    print(f"{numero2 }é o numero maior")

if numero3 > numero2 and numero3 > numero1:
    print(f"{numero3} é o numero maior") 

# numeros menores

if numero3 < numero2 and numero3 <numero1:
    print(f"{numero3} é o menor numero")

if numero2 < numero3 and numero2 < numero1:
    print(f"{numero2} é o numero maior")  

if numero1 < numero2 and numero1 < numero3:
    print(f"{numero1} é o menor numero")

