n = int(input("selecione um numero para verificacao fibonacci: "))

a,b = 0,1

while b < n:
    b,a = a+b,b

if b == n :
    print("o numero selecionado pertence a sequencia fibonacci")
else:
    print("o numero selecionado nao pertence a sequencia fibonacci")
