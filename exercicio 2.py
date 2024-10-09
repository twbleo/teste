frase = str(input("digite uma frase: "))
contador = 0

for i in range(len(frase)):
    if frase[i] == 'a':
        contador += 1

print(f"a letra 'a' aparece {contador} vezes na frase")