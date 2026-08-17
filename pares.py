numero_limite = int(input("Digite um número: "))
numeros_pares = 0
numero = 1 

while numero <= numero_limite:
    if numero % 2 == 0:
        numeros_pares += 1
    numero += 1

print(f"Do número {numero_limite} ao 1, existem {numeros_pares} números pares.")