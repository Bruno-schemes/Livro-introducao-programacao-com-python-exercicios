# fim =int(input("Digite o ultimo numero a imprimir! "))
# x = 0

# while x <= fim:
#     print(x)    x = x + 3


n = int(input("tabuada de: "))

x = int(input("Começo da tabuada: "))
f = int(input("fim da tabuada: "))

while x <= f:
    resultado = n * x
    print(f"{n} x {x} = {resultado} ")
    x = x + 1
    